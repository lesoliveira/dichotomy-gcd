"""Dicotomia como oráculo de similaridade para aprendizado em mundo aberto.

Pipeline (tudo em CPU, classificadores rasos):
  1. Dichotomizer: classificador binário "mesma classe?" treinado em pares
     |a-b| (+ a*b) de amostras das classes conhecidas (Cha & Srihari).
  2. Calibração pseudo-nova: parte das classes conhecidas finge ser nova para
     escolher (i) a taxa de aceitação de conhecidas e (ii) o corte do clustering.
     A taxa vira limiar via escores OUT-OF-FOLD dos rotulados no modelo final.
  3. Detecção: escore de uma amostra = max_c top-3 de P(mesma | x, p_cj).
  4. Descoberta: aglomerativo (average linkage) sobre 1 - P(mesma) entre as
     amostras rejeitadas; o número de classes novas sai do corte.
  5. Ruído: clusters menores que min_size (também calibrado) não viram classe
     nova; suas amostras voltam para a classe conhecida mais provável.
  6. (Variante híbrida) K̂ vem da dicotomia, mas as rejeitadas são reagrupadas com
     Ward no espaço de características.
  7. Incorporação: clusters viram protótipos; nenhum retreinamento.

Hiperparâmetros fixados a priori (sensibilidade em experiments.py --only ablation):
  AGG = "top3", NEG_RATIO = 3, PCA = 64 (em experiments.py).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import linear_sum_assignment
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import adjusted_rand_score, roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# ----------------------------------------------------------------------------- pares
def pair_features(A, B):
    """Representação de dicotomia de um par (simétrica)."""
    return np.hstack([np.abs(A - B), A * B]).astype(np.float32)


def sample_pairs(X, y, neg_ratio=3, max_pos_per_class=45, rng=None):
    rng = rng or np.random.default_rng(0)
    idx_by_c = {c: np.flatnonzero(y == c) for c in np.unique(y)}
    pos = []
    for idx in idx_by_c.values():
        ii, jj = np.triu_indices(len(idx), 1)
        sel = rng.permutation(len(ii))[:max_pos_per_class]
        pos.append(np.c_[idx[ii[sel]], idx[jj[sel]]])
    pos = np.vstack(pos)
    n_neg = neg_ratio * len(pos)
    a = rng.integers(0, len(y), 2 * n_neg)
    b = rng.integers(0, len(y), 2 * n_neg)
    keep = y[a] != y[b]
    neg = np.c_[a[keep], b[keep]][:n_neg]
    P = np.vstack([pos, neg])
    t = np.r_[np.ones(len(pos)), np.zeros(len(neg))].astype(int)
    return pair_features(X[P[:, 0]], X[P[:, 1]]), t


class EuclidLogit:
    """Ablação: mesma interface do dichotomizer, mas sem dissimilaridade aprendida.

    Do vetor do par [|a-b|, a*b] usa só a distância euclidiana ao quadrado
    d² = sum(|a-b|²) e ajusta uma logística 1-D P(mesma | d²). É apenas uma
    calibração monotônica da distância fixa (2 parâmetros), necessária para que o
    limiar, o corte e a regra de ruído operem na mesma escala de probabilidade.
    """
    def fit(self, F, t):
        self.h = F.shape[1] // 2
        self.lr = LogisticRegression(class_weight="balanced", max_iter=1000)
        self.lr.fit(self._d(F), t)
        return self

    def _d(self, F):
        return (F[:, :self.h].astype(np.float64) ** 2).sum(1, keepdims=True)

    def predict_proba(self, F):
        return self.lr.predict_proba(self._d(F))


def make_classifier(name, seed=0):
    if name == "euclid":
        return EuclidLogit()
    if name == "logreg":
        return make_pipeline(StandardScaler(),
                             LogisticRegression(C=1.0, max_iter=2000, class_weight="balanced"))
    if name == "rf":
        return RandomForestClassifier(n_estimators=200, min_samples_leaf=2, n_jobs=-1,
                                      class_weight="balanced", random_state=seed)
    if name == "hgb":
        return HistGradientBoostingClassifier(max_iter=300, learning_rate=0.1,
                                              class_weight="balanced", random_state=seed)
    raise ValueError(name)


NEG_RATIO = 3  # negativos por positivo no treino do dichotomizer


class Dichotomizer:
    def __init__(self, clf_name="logreg", seed=0, neg_ratio=None):
        self.clf_name, self.seed = clf_name, seed
        self.neg_ratio = neg_ratio or NEG_RATIO

    def fit(self, X, y):
        F, t = sample_pairs(X, y, self.neg_ratio, rng=np.random.default_rng(self.seed))
        self.clf = make_classifier(self.clf_name, self.seed).fit(F, t)
        return self

    def proba_matrix(self, A, B, chunk=200_000):
        """P(mesma classe) para todos os pares A x B."""
        n, m = len(A), len(B)
        ia, ib = np.divmod(np.arange(n * m), m)
        out = np.empty(n * m, dtype=np.float32)
        for s in range(0, n * m, chunk):
            e = min(s + chunk, n * m)
            out[s:e] = self.clf.predict_proba(pair_features(A[ia[s:e]], B[ib[s:e]]))[:, 1]
        return out.reshape(n, m)


# ------------------------------------------------------------------------- etapas
AGG = "top3"  # agregação dos protótipos de uma classe: "mean", "max" ou "topK"


def _agg(M, how):
    if how == "mean":
        return M.mean(1)
    if how == "max":
        return M.max(1)
    k = min(int(how[3:]), M.shape[1])
    return np.sort(M, 1)[:, -k:].mean(1)


OOF_FOLDS = 10  # 10 amostras/classe -> cada fold retém 1 por classe (9 protótipos restantes)


def oof_known_scores(Xl, yl, clf_name, seed, n_folds=None):
    """Escores de aceitação out-of-fold das amostras rotuladas.

    As amostras de cada classe são divididas em n_folds; para cada fold treina-se
    um dichotomizer nos demais e pontua-se o fold retido contra os protótipos dos
    demais (todas as classes). Assim nenhuma amostra é pontuada por um modelo que
    viu seus pares no treino -- o viés que fazia o limiar falhar com boosting.
    Com 10 amostras/classe e 10 folds, cada classe tem 9 protótipos (vs. 10 no
    modelo final). Com 5 folds (8 protótipos) o limiar ficava conservador: o
    modelo final aceitava ~9 pontos a mais de conhecidas do que o alvo.
    """
    n_folds = n_folds or OOF_FOLDS
    rng = np.random.default_rng(seed + 2000)
    fold = np.empty(len(yl), int)
    for c in np.unique(yl):
        idx = rng.permutation(np.flatnonzero(yl == c))
        fold[idx] = np.arange(len(idx)) % n_folds
    classes = np.unique(yl)
    out = np.empty(len(yl), np.float32)
    for f in range(n_folds):
        tr, te = fold != f, fold == f
        dic = Dichotomizer(clf_name, seed + f).fit(Xl[tr], yl[tr])
        out[te] = class_scores(dic, Xl[te], Xl[tr], yl[tr], classes).max(1)
    return out


def class_scores(dic, X, protos, proto_labels, classes, how=None):
    """Escore por classe = agregação de P(mesma) contra os protótipos da classe."""
    how = how or AGG
    P = dic.proba_matrix(X, protos)
    return np.column_stack([_agg(P[:, proto_labels == c], how) for c in classes])


def cluster_by_cut(dic, X, cut):
    """Aglomerativo average-linkage em 1-P; o número de clusters sai do corte."""
    if len(X) < 2:
        return np.zeros(len(X), int)
    P = dic.proba_matrix(X, X)
    P = (P + P.T) / 2
    D = 1.0 - P
    np.fill_diagonal(D, 0)
    ag = AgglomerativeClustering(n_clusters=None, metric="precomputed", linkage="average",
                                 distance_threshold=1.0 - cut)
    return ag.fit_predict(D)


# ------------------------------------------------------------------------ métricas
def cluster_acc(y_true, y_pred):
    """Acurácia com casamento húngaro (padrão NCD/GCD)."""
    yt = np.unique(y_true, return_inverse=True)[1]
    yp = np.unique(y_pred, return_inverse=True)[1]
    W = np.zeros((yp.max() + 1, yt.max() + 1), int)
    np.add.at(W, (yp, yt), 1)
    r, c = linear_sum_assignment(-W)
    return W[r, c].sum() / len(y_true), dict(zip(r, c))


def gcd_acc(y_true, y_pred, is_old):
    """Acurácia All/Old/New sob um único mapeamento húngaro global (Vaze et al.)."""
    yt_vals, yt = np.unique(y_true, return_inverse=True)
    yp_vals, yp = np.unique(y_pred, return_inverse=True)
    W = np.zeros((len(yp_vals), len(yt_vals)), int)
    np.add.at(W, (yp, yt), 1)
    r, c = linear_sum_assignment(-W)
    mapping = np.full(len(yp_vals), -1)
    mapping[r] = c
    hit = mapping[yp] == yt
    return hit.mean(), hit[is_old].mean(), hit[~is_old].mean()


# ------------------------------------------------------- atribuição (uso comum)
def apply_noise_rule(pred, rej, new_lab, S, classes, min_size):
    """Clusters com menos de min_size membros voltam para a classe conhecida argmax."""
    pred, rej = pred.copy(), rej.copy()
    idx_rej = np.flatnonzero(rej)
    lab_vals, counts = np.unique(new_lab, return_counts=True)
    for k, n in zip(lab_vals, counts):
        if n < min_size:
            members = idx_rej[new_lab == k]
            pred[members] = classes[S[members].argmax(1)]
            rej[members] = False
    return pred, rej


def apply_merge_back(dic, Xq, pred, rej, Xp, yp, classes, cut):
    """Cluster (>=2 membros) volta à classe c se a ligação média com c passa do corte."""
    pred, rej = pred.copy(), rej.copy()
    for k in np.unique(pred[rej]):
        members = np.flatnonzero(rej & (pred == k))
        if len(members) < 2:
            continue
        Pk = dic.proba_matrix(Xq[members], Xp)
        Sk = np.array([Pk[:, yp == c].mean() for c in classes])
        if Sk.max() >= cut:
            pred[members] = classes[Sk.argmax()]
            rej[members] = False
    return pred, rej


def detect_and_cluster(dic, Xq, Xp, yp, thr, cut, new_base):
    """Detecção + clustering das rejeitadas (antes das regras de ruído/merge)."""
    classes = np.unique(yp)
    S = class_scores(dic, Xq, Xp, yp, classes)
    score = S.max(1)
    pred = classes[S.argmax(1)].astype(int)
    rej = score < thr
    new_lab = cluster_by_cut(dic, Xq[rej], cut)
    pred[rej] = new_base + new_lab
    return dict(S=S, score=score, pred=pred, rej=rej, new_lab=new_lab, classes=classes)


# ------------------------------------------------------------ calibração pseudo-nova
@dataclass
class Calib:
    reject_thr: float   # limiar absoluto no cenário pseudo (apenas diagnóstico)
    known_tpr: float    # fração de amostras conhecidas aceitas no ponto escolhido
    cut: float          # corte do aglomerativo em P(mesma classe)
    min_size: int       # tamanho mínimo de um cluster para virar classe nova


MIN_SIZE_GRID = (1, 2, 3, 4, 5, 6)


def calibrate(Xl, yl, clf_name, seed, frac=0.25, n_proto=6):
    """Simula o mundo aberto dentro das classes conhecidas.

    75 % das classes: n_proto protótipos + o resto como teste "conhecido".
    25 % das classes: pseudo-novas (todas as amostras).
    Escolhe, nesta ordem: limiar (Youden J), corte (ARI nas pseudo-novas) e
    min_size (acurácia GCD no conjunto pseudo completo, detecção real).
    """
    rng = np.random.default_rng(seed + 1000)
    classes = np.unique(yl)
    pseudo = rng.choice(classes, max(2, int(frac * len(classes))), replace=False)
    kn = np.setdiff1d(classes, pseudo)
    m_kn, m_ps = np.isin(yl, kn), np.isin(yl, pseudo)
    proto_mask = np.zeros(len(yl), bool)
    for c in kn:
        idx = np.flatnonzero(yl == c)
        proto_mask[rng.permutation(idx)[:n_proto]] = True
    Xp, yp = Xl[proto_mask], yl[proto_mask]
    dic = Dichotomizer(clf_name, seed).fit(Xp, yp)
    test_known = m_kn & ~proto_mask
    Xq = np.vstack([Xl[test_known], Xl[m_ps]])
    yq = np.r_[yl[test_known], yl[m_ps]]
    is_new = np.r_[np.zeros(test_known.sum()), np.ones(m_ps.sum())].astype(bool)
    S = class_scores(dic, Xq, Xp, yp, kn).max(1)
    # (i) limiar de rejeição: Youden J. As amostras de teste conhecidas não
    # participaram do treino, então a taxa de aceitação é honesta.
    grid = np.quantile(S, np.linspace(0.01, 0.99, 99))
    J = [((S[~is_new] >= t).mean() + (S[is_new] < t).mean()) for t in grid]
    reject_thr = float(grid[int(np.argmax(J))])
    known_tpr = float((S[~is_new] >= reject_thr).mean())
    # (ii) corte do clustering: ARI entre as pseudo-novas (detecção oráculo)
    Xn, yn = Xl[m_ps], yl[m_ps]
    P = dic.proba_matrix(Xn, Xn)
    D = 1 - (P + P.T) / 2
    np.fill_diagonal(D, 0)
    best = (-1, 0.5)
    for cut in np.linspace(0.05, 0.95, 19):
        lab = AgglomerativeClustering(n_clusters=None, metric="precomputed", linkage="average",
                                      distance_threshold=1 - cut).fit_predict(D)
        best = max(best, (adjusted_rand_score(yn, lab), float(cut)))
    cut = best[1]
    # (iii) min_size: pipeline completo no cenário pseudo, escolhe o melhor GCD-All
    R = detect_and_cluster(dic, Xq, Xp, yp, reject_thr, cut, new_base=yl.max() + 1)
    best_m = (-1, 0, 1)
    for m in MIN_SIZE_GRID:
        pred, _ = apply_noise_rule(R["pred"], R["rej"], R["new_lab"], R["S"], R["classes"], m)
        acc = gcd_acc(yq, pred, ~is_new)[0]
        best_m = max(best_m, (acc, -m, m))        # empate -> menor min_size
    return Calib(reject_thr, known_tpr, cut, best_m[2])


# --------------------------------------------------------------------- pipeline OWL
def regroup_euclidean(Xq, pred, rej, new_base):
    """Variante híbrida: mantém QUAIS amostras são novas e QUANTAS classes (K̂, da
    dicotomia + regra de ruído), mas refaz o agrupamento das rejeitadas com Ward
    no espaço de características, com K̂ grupos."""
    pred = pred.copy()
    k_hat = len(np.unique(pred[rej]))
    if k_hat >= 2 and rej.sum() > k_hat:
        lab = AgglomerativeClustering(k_hat, linkage="ward").fit_predict(Xq[rej])
        pred[rej] = new_base + lab
    return pred


def run_open_world(Xl, yl, Xu, clf_name="logreg", seed=0, calib: Calib | None = None,
                   noise=True, merge_back=False, hybrid=False, dic=None, oof=None):
    """Detecta, descobre e incorpora.

    noise: aplica a regra de ruído com o min_size calibrado.
    hybrid: depois do ruído, reagrupa as rejeitadas com Ward usando o K̂ da dicotomia.
    merge_back: ablação; clusters >=2 voltam a uma classe conhecida se a ligação
    média com ela passa do corte (absorve classes novas reais; não recomendado).
    """
    calib = calib or calibrate(Xl, yl, clf_name, seed)
    dic = dic or Dichotomizer(clf_name, seed).fit(Xl, yl)
    # O limiar absoluto do cenário pseudo não transfere (mais classes e
    # protótipos deslocam os escores). Transferimos a TAXA DE ACEITAÇÃO de
    # conhecidas, aplicada à distribuição out-of-fold sob a configuração final.
    if oof is None:
        oof = oof_known_scores(Xl, yl, clf_name, seed)
    thr = float(np.quantile(oof, 1.0 - calib.known_tpr))
    R = detect_and_cluster(dic, Xu, Xl, yl, thr, calib.cut, new_base=yl.max() + 1)
    pred, rej = R["pred"], R["rej"]
    if noise:
        pred, rej = apply_noise_rule(pred, rej, R["new_lab"], R["S"], R["classes"],
                                     calib.min_size)
    if merge_back:
        pred, rej = apply_merge_back(dic, Xu, pred, rej, Xl, yl, R["classes"], calib.cut)
    if hybrid:
        pred = regroup_euclidean(Xu, pred, rej, new_base=yl.max() + 1)
    # incorporação: banco de protótipos estendido, sem retreino
    protos = np.vstack([Xl, Xu[rej]])
    proto_y = np.r_[yl, pred[rej]]
    return dict(pred=pred, score=R["score"], rejected=rej, rejected_raw=R["rej"], dic=dic,
                calib=calib, thr=thr, oof=oof, protos=protos, proto_y=proto_y,
                n_new=len(np.unique(pred[rej])) if rej.any() else 0)


def classify_with_bank(dic, X, protos, proto_y):
    classes = np.unique(proto_y)
    S = class_scores(dic, X, protos, proto_y, classes)
    return classes[S.argmax(1)]
