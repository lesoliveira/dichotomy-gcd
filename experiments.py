"""Experimentos de mundo aberto. Dichotomizer, calibração e clustering em CPU.

Protocolo por semente (detalhes no README):
  * Omniglot: 100 classes (caracteres) conhecidas do background; 20 novas:
    "near" = outros caracteres do background, "far" = alfabetos do evaluation.
  * Séries UCR (features_ts.py): novidade "random"; por padrão 2/3 das classes
    conhecidas e 1/3 novas. Features MiniRocket ajustadas só em L, por semente.
  * conhecidas: 10 rotuladas (L) / 7 não rotuladas (U) / 3 teste (T) por classe.
  * novas:      15 em U / 5 em T por classe.

Experimentos (--only):
  main      detecção, descoberta, GCD ponta a ponta e calibração
  transfer  RQ1: AUC do dichotomizer em pares de classes novas vs. nº de conhecidas
  ablation  sensibilidade aos hiperparâmetros fixados a priori (só logreg)

As sementes começam em --seed0 (padrão 10): as sementes 0-4 foram usadas no
desenvolvimento do método e não entram nos resultados finais.

    python experiments.py --features omniglot_dinov2.npz --seeds 5
"""
import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import adjusted_rand_score, roc_auc_score, silhouette_score
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

import dichotomy_owl as do

HERE = Path(__file__).parent
FEATS = HERE / "omniglot_hog.npz"
OUT = HERE / "results"
N_PCA = 64
NOVELTIES = ("near", "far")
N_KNOWN, N_NEW = 100, 20
PREP_FIT = "LU"   # onde ajustar o pré-processamento não supervisionado: "L" ou "LU"
WHITEN = False    # PCA sem whitening (escolhido em choose_prep.py, sementes de desenvolvimento)


# ------------------------------------------------------------------------- dados
def is_ssb(data):
    """CUB com os splits do Semantic Shift Benchmark (features_cub.py)."""
    return bool((data["split"] == "known").any())


def load():
    """Dados como dict: X (features) ou series (séries brutas), y, split."""
    d = np.load(FEATS)
    data = dict(y=d["y"], split=d["split"])
    if "series" in d.files:
        data["series"] = d["series"]
    else:
        data["X"] = d["X"]
    return data


def minirocket_features(series, fit_idx, seed):
    """MiniRocket com kernels/vieses ajustados só nas séries de fit_idx (= L)."""
    from aeon.transformations.collection.convolution_based import MiniRocket
    mr = MiniRocket(n_kernels=10_000, random_state=seed, n_jobs=-1)
    mr.fit(series[fit_idx][:, None, :])
    return mr.transform(series[:, None, :]).astype(np.float32)


def make_split(data, n_known, n_new, novelty, seed, n_comp=None):
    y, split = data["y"], data["split"]
    rng = np.random.default_rng(seed)
    if novelty == "random":
        allc = np.unique(y)
        known = rng.choice(allc, n_known, replace=False)
        new = rng.choice(np.setdiff1d(allc, known), n_new, replace=False)
    elif is_ssb(data):
        # Semantic Shift Benchmark: conhecidas das 100 "known"; near = Hard (mais
        # parecidas com as conhecidas), far = Easy (mais diferentes). Medium fica de fora.
        known = rng.choice(np.unique(y[split == "known"]), n_known, replace=False)
        pool = np.unique(y[split == ("hard" if novelty == "near" else "easy")])
        new = rng.choice(pool, n_new, replace=False)
    else:
        bg = np.unique(y[split == "images_background"])
        ev = np.unique(y[split == "images_evaluation"])
        known = rng.choice(bg, n_known, replace=False)
        pool = np.setdiff1d(bg, known) if novelty == "near" else ev
        new = rng.choice(pool, n_new, replace=False)
    L, U, T = [], [], []
    for c in known:
        idx = rng.permutation(np.flatnonzero(y == c))
        L += list(idx[:10]); U += list(idx[10:17]); T += list(idx[17:20])
    for c in new:
        idx = rng.permutation(np.flatnonzero(y == c))
        U += list(idx[:15]); T += list(idx[15:20])
    L, U, T = map(np.array, (L, U, T))
    # Pré-processamento NÃO supervisionado (MiniRocket, escala, PCA) ajustado em L ∪ U
    # (padrão, transdutivo como no GCD: U está disponível sem rótulos no treino) ou só
    # em L (--prep-fit L, protocolo das versões <= 4). T nunca entra.
    fit = np.r_[L, U] if PREP_FIT == "LU" else L
    X = data["X"] if "X" in data else minirocket_features(data["series"], fit, seed)
    prep = make_prep(X[fit], seed, n_comp)
    Z = prep(X)
    return dict(Xl=Z[L], yl=y[L], Xu=Z[U], yu=y[U], Xt=Z[T], yt=y[T], known=known, new=new)


def make_prep(Xl, seed, n_comp=None):
    """StandardScaler + PCA (sem whitening por padrão), ajustados em Xl (L ou L ∪ U).

    Whitening foi abandonado na versão 6: com 64 componentes ajustados em L ∪ U ele
    amplifica direções de ruído e degradava os baselines euclidianos nas séries
    (k-means com K oráculo no SwedishLeaf: 0,80 sem whitening vs. 0,38 com). A escolha
    foi feita em choose_prep.py com sementes de desenvolvimento (0-2), olhando SÓ para
    os baselines (k-means e Ward com K oráculo), nunca para o método proposto.

    Componentes limitados a n/4. Ajustar só em L com poucas classes conhecidas
    degenera a representação: dimensões quase constantes em L (comuns no HOG)
    explodem na padronização e no whitening (|z| > 10^4 com 25 classes), e todo
    agrupamento de classes novas colapsa. Por isso o padrão é L ∪ U.
    """
    n_comp = min(n_comp or N_PCA, max(2, len(Xl) // 4))
    sc = StandardScaler().fit(Xl)
    pca = PCA(n_comp, whiten=WHITEN, random_state=seed).fit(sc.transform(Xl))
    return lambda A: pca.transform(sc.transform(A)).astype(np.float32)


# ---------------------------------------------------------------------- baselines
def sqdist(A, B):
    """Distâncias euclidianas ao quadrado sem tensores n x m x d (memória O(n m))."""
    A = A.astype(np.float64); B = B.astype(np.float64)
    D = (A * A).sum(1)[:, None] + (B * B).sum(1)[None] - 2 * A @ B.T
    return np.maximum(D, 0)


def ss_kmeans(Xl, yl, Xu, k_total, seed, iters=50):
    """k-means semissupervisionado (Vaze et al., GCD): rotulados presos à sua classe."""
    rng = np.random.default_rng(seed)
    classes = np.unique(yl)
    C = np.vstack([Xl[yl == c].mean(0) for c in classes])
    extra = []                                     # k-means++ para os centróides extras
    dmin = sqdist(Xu, C).min(1)
    for _ in range(k_total - len(classes)):
        c = Xu[rng.choice(len(Xu), p=dmin / dmin.sum())][None]
        extra.append(c)
        dmin = np.minimum(dmin, sqdist(Xu, c)[:, 0])
    C = np.vstack([C] + extra)
    lab_l = np.searchsorted(classes, yl)
    for _ in range(iters):
        lu = sqdist(Xu, C).argmin(1)
        newC = C.copy()
        for k in range(len(C)):
            pts = np.vstack([Xl[lab_l == k], Xu[lu == k]])
            if len(pts):
                newC[k] = pts.mean(0)
        if np.allclose(newC, C):
            break
        C = newC
    pred = np.where(lu < len(classes), classes[np.minimum(lu, len(classes) - 1)], 10_000 + lu)
    return pred, C, classes


def estimate_k(Xl, yl, Xu, seed, kmax=None):
    """Estimativa de K do GCD (Vaze et al., 2022): k-means em L ∪ U para cada K
    candidato; escolhe o K que maximiza a acurácia húngara no subconjunto rotulado.
    Busca em grade grossa + refinamento (no lugar do método de Brent)."""
    n_known = len(np.unique(yl))
    Xa = np.vstack([Xl, Xu])
    kmin = n_known + 1
    kmax = min(kmax or 3 * n_known, len(Xa) // 3)
    cache = {}

    def score(k):
        if k not in cache:
            lab = KMeans(k, n_init=3, random_state=seed).fit_predict(Xa)
            cache[k] = do.cluster_acc(yl, lab[:len(Xl)])[0]
        return cache[k]
    step = max(1, (kmax - kmin) // 15)
    best = max(range(kmin, kmax + 1, step), key=score)
    for k in range(max(kmin, best - step + 1), min(kmax, best + step - 1) + 1):
        score(k)
    return max(cache, key=lambda k: (cache[k], -k))


def proto_classify_euclid(X, protos, proto_y, k=3):
    """Mesmo classificador por protótipos do método (top-k), mas com distância euclidiana."""
    D = sqdist(X, protos)
    classes = np.unique(proto_y)
    S = np.column_stack([-np.sort(D[:, proto_y == c], 1)[:, :k].mean(1) for c in classes])
    return classes[S.argmax(1)]


def kmeans_sil(X, kmax, seed):
    best = (-1, 2, None)
    for k in range(2, kmax + 1, max(1, kmax // 15)):
        lab = KMeans(k, n_init=3, random_state=seed).fit_predict(X)
        best = max(best, (silhouette_score(X, lab), k, lab), key=lambda t: t[0])
    return best[2], best[1]


# ----------------------------------------------------------------- experimento 1
VARIANTS = [("", dict(noise=False, merge_back=False)),          # base
            (" + ruído", dict(noise=True, merge_back=False)),   # proposto
            (" + merge-back", dict(noise=False, merge_back=True)),  # ablação
            (" + híbrido", dict(noise=True, hybrid=True))]       # K da dicotomia + Ward


def exp_main(data, seeds, clfs, seed0, n_known, n_new):
    rows_det, rows_disc, rows_gcd = [], [], []
    for novelty in NOVELTIES:
        for seed in range(seed0, seed0 + seeds):
            D = make_split(data, n_known, n_new, novelty, seed)
            Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
            is_new_u = np.isin(yu, D["new"])
            is_old_t = np.isin(yt, D["known"])
            classes = np.unique(yl)
            Cm = np.vstack([Xl[yl == c].mean(0) for c in classes])
            base = dict(novelty=novelty, seed=seed)

            # ---- baselines de detecção
            d_cent = sqdist(Xu, Cm).min(1)
            d_nn = sqdist(Xu, Xl).min(1)
            msp = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=0.1)).fit(Xl, yl).predict_proba(Xu).max(1)
            for name, s in [("centroid-dist", -d_cent), ("1NN-dist", -d_nn), ("LR-MSP", msp)]:
                rows_det.append(dict(base, method=name, auroc=roc_auc_score(~is_new_u, s)))

            # ---- descoberta com detecção oráculo (só as novas de U)
            Xn, yn = Xu[is_new_u], yu[is_new_u]
            K = n_new

            def disc(name, lab, k_est):
                rows_disc.append(dict(base, method=name, acc=do.cluster_acc(yn, lab)[0],
                                      ari=adjusted_rand_score(yn, lab), k_est=k_est, k_true=K))
            disc("kmeans (K oráculo)", KMeans(K, n_init=10, random_state=seed).fit_predict(Xn), K)
            lab, k = kmeans_sil(Xn, 3 * K, seed)
            disc("kmeans (K silhueta)", lab, k)
            disc("aglom. ward (K oráculo)",
                 AgglomerativeClustering(K, linkage="ward").fit_predict(Xn), K)
            nca = NeighborhoodComponentsAnalysis(min(32, Xl.shape[1]), random_state=seed,
                                                max_iter=50).fit(Xl, yl)
            disc("NCA + kmeans (K oráculo)",
                 KMeans(K, n_init=10, random_state=seed).fit_predict(nca.transform(Xn)), K)

            # ---- baseline GCD ponta a ponta (dois classificadores de teste)
            pred_ss, C, _ = ss_kmeans(Xl, yl, Xu, n_known + n_new, seed)
            a, o, n = do.gcd_acc(yu, pred_ss, ~is_new_u)
            lt = sqdist(Xt, C).argmin(1)
            pt_c = np.where(lt < len(classes), classes[np.minimum(lt, len(classes) - 1)],
                            10_000 + lt)
            pt_p = proto_classify_euclid(Xt, np.vstack([Xl, Xu]), np.r_[yl, pred_ss])
            for name, pt in [("SS-kmeans (K oráculo)", pt_c),
                             ("SS-kmeans + protótipos (K oráculo)", pt_p)]:
                ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
                rows_gcd.append(dict(base, method=name, all=a, old=o, new=n, k_est=n_new,
                                     test_all=ta, test_old=to, test_new=tn))
            # GCD realista: K estimado pelo procedimento de Vaze et al.
            k_hat = estimate_k(Xl, yl, Xu, seed)
            pred_se, C, _ = ss_kmeans(Xl, yl, Xu, k_hat, seed)
            a, o, n = do.gcd_acc(yu, pred_se, ~is_new_u)
            lt = sqdist(Xt, C).argmin(1)
            pt = np.where(lt < len(classes), classes[np.minimum(lt, len(classes) - 1)], 10_000 + lt)
            ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
            rows_gcd.append(dict(base, method="SS-kmeans (K estimado)", all=a, old=o, new=n,
                                 k_est=k_hat - n_known, test_all=ta, test_old=to, test_new=tn))

            # ---- método proposto
            for clf in clfs:
                t0 = time.time()
                calib = do.calibrate(Xl, yl, clf, seed)
                dic, oof = None, None
                for suffix, kw in VARIANTS:
                    R = do.run_open_world(Xl, yl, Xu, clf, seed, calib, dic=dic, oof=oof, **kw)
                    dic, oof = R["dic"], R["oof"]
                    if suffix == "":
                        rows_det.append(dict(base, method=f"dicotomia-{clf}",
                                             auroc=roc_auc_score(~is_new_u, R["score"])))
                        lab = do.cluster_by_cut(dic, Xn, calib.cut)
                        k_auto = len(np.unique(lab))
                        disc(f"dicotomia-{clf} (K auto)", lab, k_auto)
                        disc(f"dicotomia-{clf} K auto + Ward",
                             AgglomerativeClustering(k_auto, linkage="ward").fit_predict(Xn)
                             if k_auto >= 2 else lab, k_auto)
                    a, o, n = do.gcd_acc(yu, R["pred"], ~is_new_u)
                    pt = do.classify_with_bank(dic, Xt, R["protos"], R["proto_y"])
                    ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
                    rej = R["rejected"]
                    rows_gcd.append(dict(base, method=f"dicotomia-{clf}{suffix}",
                                         all=a, old=o, new=n, k_est=R["n_new"],
                                         test_all=ta, test_old=to, test_new=tn,
                                         cut=calib.cut, min_size=calib.min_size,
                                         rej_rate=rej.mean(), true_new_rate=is_new_u.mean(),
                                         rej_recall_new=rej[is_new_u].mean(),
                                         known_tpr_target=calib.known_tpr,
                                         known_tpr_obs=1 - R["rejected_raw"][~is_new_u].mean(),
                                         secs=time.time() - t0))
            print(f"[{novelty} seed {seed}] ok", flush=True)
    return pd.DataFrame(rows_det), pd.DataFrame(rows_disc), pd.DataFrame(rows_gcd)


# ----------------------------------------------------------------- experimento 2
def exp_transfer(data, seeds, seed0, clf="logreg"):
    """RQ1: o dichotomizer generaliza para pares de classes nunca vistas?"""
    n_cls = len(np.unique(data["y"]))
    n_new = min(50, max(3, n_cls // 3))
    if NOVELTIES == ("random",):
        grid = [k for k in (3, 5, 10, 15, 20, 25, 30, 40, 50) if k <= n_cls - n_new]
    else:
        grid = [5, 10, 25, 50, 100, 200, 400]
    if is_ssb(data):        # 100 classes conhecidas; o menor grupo novo (Easy) tem 32
        grid, n_new = [5, 10, 25, 50, 100], 20
    rows = []
    for seed in range(seed0, seed0 + seeds):
        for n_known in grid:
            for novelty in NOVELTIES:
                D = make_split(data, n_known, n_new, novelty, seed)
                dic = do.Dichotomizer(clf, seed).fit(D["Xl"], D["yl"])
                m = np.isin(D["yu"], D["new"])
                Xn, yn = D["Xu"][m], D["yu"][m]
                P = dic.proba_matrix(Xn, Xn)
                iu = np.triu_indices(len(yn), 1)
                same = (yn[:, None] == yn[None])[iu]
                rows.append(dict(seed=seed, n_known=n_known, novelty=novelty,
                                 pca_dims=D["Xl"].shape[1],
                                 pair_auc_new=roc_auc_score(same, P[iu])))
        print(f"[transfer seed {seed}] ok", flush=True)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------- experimento 4
def exp_scale(data, seeds, seed0, n_new, grid=None, clf="hgb"):
    """Escala: varia o nº de classes conhecidas DENTRO do mesmo conjunto, ponta a ponta.

    Para cada n_known: dicotomia + ruído, dicotomia + híbrido, SS-kmeans com K estimado
    (busca até n_known + |U|/10 classes, limite que só usa o tamanho de U) e com K
    oráculo; descoberta com detecção oráculo; AUROC de detecção.
    """
    n_cls = len(np.unique(data["y"]))
    if grid is None:
        if NOVELTIES == ("random",):
            grid = [k for k in (5, 10, 15, 20, 25, 30, 40) if k <= n_cls - n_new]
        else:
            grid = [10, 25, 50, 100] if is_ssb(data) else [10, 25, 50, 100, 200]
    rows = []
    for seed in range(seed0, seed0 + seeds):
        for n_known in grid:
            for novelty in NOVELTIES:
                t0 = time.time()
                D = make_split(data, n_known, n_new, novelty, seed)
                Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
                is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
                classes = np.unique(yl)
                base = dict(novelty=novelty, seed=seed, n_known=n_known, n_new=n_new)

                def gcd_row(name, pred_u, pred_t, k_est):
                    a, o, n = do.gcd_acc(yu, pred_u, ~is_new_u)
                    ta, to, tn = do.gcd_acc(yt, pred_t, is_old_t)
                    rows.append(dict(base, kind="gcd", method=name, all=a, old=o, new=n,
                                     test_all=ta, test_old=to, test_new=tn, k_est=k_est,
                                     k_err=abs(k_est - n_new)))
                for name, k_tot in [("SS-kmeans (K oráculo)", n_known + n_new),
                                    ("SS-kmeans (K estimado)",
                                     estimate_k(Xl, yl, Xu, seed, kmax=n_known + len(Xu) // 10))]:
                    pu, C, _ = ss_kmeans(Xl, yl, Xu, k_tot, seed)
                    lt = sqdist(Xt, C).argmin(1)
                    pt = np.where(lt < len(classes), classes[np.minimum(lt, len(classes) - 1)],
                                  10_000 + lt)
                    gcd_row(name, pu, pt, k_tot - n_known)
                calib = do.calibrate(Xl, yl, clf, seed)
                R = do.run_open_world(Xl, yl, Xu, clf, seed, calib, noise=True)
                for suffix, kw in [(" + ruído", {}), (" + híbrido", dict(hybrid=True))]:
                    if kw:
                        R = do.run_open_world(Xl, yl, Xu, clf, seed, calib, noise=True,
                                              dic=R["dic"], oof=R["oof"], **kw)
                    pt = do.classify_with_bank(R["dic"], Xt, R["protos"], R["proto_y"])
                    gcd_row(f"dicotomia-{clf}{suffix}", R["pred"], pt, R["n_new"])
                # detecção
                msp = make_pipeline(StandardScaler(), LogisticRegression(max_iter=3000, C=0.1)).fit(Xl, yl).predict_proba(Xu).max(1)
                for name, sc in [(f"dicotomia-{clf}", R["score"]), ("LR-MSP", msp)]:
                    rows.append(dict(base, kind="det", method=name,
                                     auroc=roc_auc_score(~is_new_u, sc)))
                # descoberta com detecção oráculo
                Xn, yn = Xu[is_new_u], yu[is_new_u]
                lab = do.cluster_by_cut(R["dic"], Xn, calib.cut)
                k_auto = len(np.unique(lab))
                for name, lb, k in [
                        (f"dicotomia-{clf} (K auto)", lab, k_auto),
                        (f"dicotomia-{clf} K auto + Ward",
                         AgglomerativeClustering(k_auto, linkage="ward").fit_predict(Xn)
                         if k_auto >= 2 else lab, k_auto),
                        ("kmeans (K oráculo)",
                         KMeans(n_new, n_init=10, random_state=seed).fit_predict(Xn), n_new)]:
                    rows.append(dict(base, kind="desc", method=name,
                                     acc=do.cluster_acc(yn, lb)[0], k_est=k))
                print(f"[escala n_known={n_known} {novelty} seed {seed}] {time.time() - t0:.0f}s",
                      flush=True)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------- experimento 3
ABLATION = [  # (fator, valor, AGG, NEG_RATIO, PCA); a primeira linha é o padrão
    ("padrão", "top3 / 3:1 / 64", "top3", 3, 64),
    ("agregação", "mean", "mean", 3, 64),
    ("agregação", "max", "max", 3, 64),
    ("agregação", "top5", "top5", 3, 64),
    ("negativos", "1:1", "top3", 1, 64),
    ("negativos", "5:1", "top3", 5, 64),
    ("PCA", "32", "top3", 3, 32),
    ("PCA", "128", "top3", 3, 128),
]


def exp_ablation(data, seeds, seed0, n_known, n_new, clf="logreg"):
    rows = []
    defaults = (do.AGG, do.NEG_RATIO)
    try:
        for factor, value, agg, neg, pca in ABLATION:
            do.AGG, do.NEG_RATIO = agg, neg
            for novelty in NOVELTIES:
                for seed in range(seed0, seed0 + seeds):
                    D = make_split(data, n_known, n_new, novelty, seed, n_comp=pca)
                    Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
                    is_new_u = np.isin(yu, D["new"])
                    calib = do.calibrate(Xl, yl, clf, seed)
                    R = do.run_open_world(Xl, yl, Xu, clf, seed, calib, noise=True)
                    Xn, yn = Xu[is_new_u], yu[is_new_u]
                    lab = do.cluster_by_cut(R["dic"], Xn, calib.cut)
                    pt = do.classify_with_bank(R["dic"], Xt, R["protos"], R["proto_y"])
                    ta, to, tn = do.gcd_acc(yt, pt, np.isin(yt, D["known"]))
                    rows.append(dict(factor=factor, value=value, novelty=novelty, seed=seed,
                                     auroc=roc_auc_score(~is_new_u, R["score"]),
                                     disc_acc=do.cluster_acc(yn, lab)[0],
                                     disc_k=len(np.unique(lab)), k_est=R["n_new"],
                                     test_all=ta, test_new=tn))
            print(f"[ablation {factor}={value}] ok", flush=True)
    finally:
        do.AGG, do.NEG_RATIO = defaults
    return pd.DataFrame(rows)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--seed0", type=int, default=10,
                    help="primeira semente (0-4 foram usadas no desenvolvimento)")
    ap.add_argument("--clfs", default="logreg,hgb")
    ap.add_argument("--only", default="all",
                    help="lista separada por vírgulas: main, transfer, ablation, scale "
                         "(all = main,transfer,ablation)")
    ap.add_argument("--scale-grid", default=None,
                    help="nº de classes conhecidas no experimento de escala, ex.: 10,25,50,100,200")
    ap.add_argument("--scale-clf", default="hgb")
    ap.add_argument("--transfer-clf", default="logreg",
                    help="dichotomizer da RQ1 (padrão logreg, como nas versões anteriores; hgb = o do método)")
    ap.add_argument("--whiten", action="store_true",
                    help="PCA com whitening (protocolo das versões <= 5)")
    ap.add_argument("--prep-fit", default="LU", choices=["LU", "L"],
                    help="ajuste do pré-processamento não supervisionado (padrão L ∪ U)")
    ap.add_argument("--features", default=str(FEATS),
                    help="arquivo .npz de features.py ou features_cnn.py")
    ap.add_argument("--pca", type=int, default=64, help="componentes do PCA (ajustado só em L)")
    ap.add_argument("--out", default=None, help="pasta de saída (padrão: results/<features>)")
    ap.add_argument("--n-known", type=int, default=None,
                    help="classes conhecidas (padrão: 100 no Omniglot; 2/3 das classes nas séries)")
    ap.add_argument("--n-new", type=int, default=None,
                    help="classes novas (padrão: 20 no Omniglot; 1/3 das classes nas séries)")
    args = ap.parse_args()
    FEATS = Path(args.features)
    N_PCA = args.pca
    PREP_FIT = args.prep_fit
    WHITEN = args.whiten
    OUT = Path(args.out) if args.out else HERE / "results" / FEATS.stem
    OUT.mkdir(parents=True, exist_ok=True)
    data = load()
    if "series" in data:                       # séries UCR: novidade aleatória
        NOVELTIES = ("random",)
        n_cls = len(np.unique(data["y"]))
        N_NEW = args.n_new or round(n_cls / 3)
        N_KNOWN = args.n_known or n_cls - N_NEW
    else:
        N_KNOWN, N_NEW = args.n_known or N_KNOWN, args.n_new or N_NEW
    print(f"{FEATS.stem}: {N_KNOWN} conhecidas, {N_NEW} novas, cenários {NOVELTIES}, "
          f"pré-processamento em {PREP_FIT}, whitening={WHITEN}, sementes {args.seed0}-{args.seed0 + args.seeds - 1}",
          flush=True)
    only = {"main", "transfer", "ablation"} if args.only == "all" else set(args.only.split(","))
    if "main" in only:
        det, disc, gcd = exp_main(data, args.seeds, args.clfs.split(","), args.seed0,
                                  N_KNOWN, N_NEW)
        det.to_csv(OUT / "deteccao.csv", index=False)
        disc.to_csv(OUT / "descoberta.csv", index=False)
        gcd.to_csv(OUT / "gcd.csv", index=False)
    if "transfer" in only:
        exp_transfer(data, args.seeds, args.seed0, clf=args.transfer_clf).to_csv(
            OUT / f"transferencia{'' if args.transfer_clf == 'logreg' else '_' + args.transfer_clf}.csv",
            index=False)
    if "ablation" in only:
        exp_ablation(data, args.seeds, args.seed0, N_KNOWN, N_NEW).to_csv(OUT / "ablacao.csv",
                                                                          index=False)
    if "scale" in only:
        grid = [int(k) for k in args.scale_grid.split(",")] if args.scale_grid else None
        exp_scale(data, args.seeds, args.seed0, N_NEW, grid, args.scale_clf).to_csv(
            OUT / "escala.csv", index=False)
