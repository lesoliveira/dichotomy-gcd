"""Experimentos pedidos na revisão (paperreview.ai), no protocolo final (sementes 20-24).

    python experiments_review.py --features omniglot_dinov2.npz --only simgcd,cluster,ablation

Três experimentos, cada um gravado em results_review/<features>/:

simgcd.csv      Comparação com um GCD moderno sobre as MESMAS features fixas: a cabeça
                paramétrica do SimGCD (Wen et al., ICCV 2023), isto é, classificador de
                cosseno com supervisão em L, autodestilação entre duas "vistas" e
                regularização de entropia média, treinada sobre a representação congelada
                (sem ajustar o backbone, como todos os métodos do artigo). K estimado pelo
                procedimento de Vaze et al. e K oráculo; com e sem whitening, para o
                critério conservador (o baseline recebe o melhor dos dois).

agrupamento.csv Outras formas de transformar P(mesma classe) em grupos. Com detecção
                oráculo (só as novas de U) e com o K̂ da própria dicotomia:
                average linkage (o método), espectral sobre a matriz P, Ward e k-means no
                espaço de características. Também ponta a ponta: o pipeline completo com
                as rejeitadas reagrupadas por cada alternativa (mesmo K̂).

ablacao_final.csv  Sensibilidade no protocolo final, com o dichotomizer do método (hgb):
                agregação (top1, top5, mean), negativos (1:1, 5:1, difíceis), PCA (128),
                fração de pseudo-novas (15 %, 40 %) e ligação (single, complete).
                A linha "padrão" reproduz o método.

Nada aqui altera dichotomy_owl.py ou experiments.py: as variantes são aplicadas
temporariamente e restauradas ao final de cada configuração.
"""
import argparse
import time
from contextlib import contextmanager
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans, SpectralClustering
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import NearestNeighbors

import dichotomy_owl as do
import experiments as E

CLF = "hgb"


# ----------------------------------------------------------------- dados / split
def setup(features, pca=64, n_known_arg=None, n_new_arg=None):
    E.FEATS = Path(features)
    E.N_PCA = pca
    data = E.load()
    if "series" in data:
        E.NOVELTIES = ("random",)
        n_cls = len(np.unique(data["y"]))
        n_new = round(n_cls / 3)
        n_known = n_cls - n_new
    else:
        E.NOVELTIES = ("near", "far")
        n_known, n_new = 100, 20
    return data, n_known_arg or n_known, n_new_arg or n_new


def split(data, n_known, n_new, novelty, seed, whiten=False, n_comp=None):
    old = E.WHITEN
    E.WHITEN = whiten
    try:
        return E.make_split(data, n_known, n_new, novelty, seed, n_comp=n_comp)
    finally:
        E.WHITEN = old


# ------------------------------------------------------------- 1. SimGCD raso
def simgcd_shallow(Xl, yl, Xu, Xt, k_total, seed, epochs=200, hidden=256,
                   sup_w=0.35, memax_w=2.0, tau_s=0.1, tau_t=(0.07, 0.04), warmup=30,
                   noise=0.1, drop=0.1, lr=1e-3, batch=256):
    """Cabeça paramétrica do SimGCD sobre features congeladas (CPU).

    Projeção MLP + classificador de cosseno com k_total protótipos. Perda =
    sup_w * CE(rotulados) + (1 - sup_w) * [autodestilação entre duas vistas
    - memax_w * entropia da predição média]. As vistas são o mesmo vetor com ruído
    gaussiano e dropout de atributos (não há aumento de imagem com features fixas).
    Hiperparâmetros do SimGCD: sup_w = 0.35, temperatura do professor 0.07 -> 0.04
    nas primeiras 30 épocas, aluno 0.1. Retorna rótulos para U e T; as classes
    conhecidas ocupam os índices 0..C-1 da cabeça e voltam ao rótulo original.
    """
    import torch
    import torch.nn.functional as F
    torch.set_num_threads(1)        # rede minúscula: mais threads só disputam a CPU
    torch.manual_seed(seed)
    classes = np.unique(yl)
    C = len(classes)
    k_total = max(k_total, C + 1)
    yl_idx = np.searchsorted(classes, yl)
    X = torch.tensor(np.vstack([Xl, Xu]), dtype=torch.float32)
    is_l = torch.zeros(len(X), dtype=torch.bool)
    is_l[:len(Xl)] = True
    ylab = torch.full((len(X),), -1, dtype=torch.long)
    ylab[:len(Xl)] = torch.tensor(yl_idx)
    sd = X.std(0, keepdim=True)
    proj = torch.nn.Sequential(torch.nn.Linear(X.shape[1], hidden), torch.nn.GELU(),
                               torch.nn.Linear(hidden, hidden))
    W = torch.nn.Parameter(torch.randn(k_total, hidden) * 0.01)
    opt = torch.optim.Adam(list(proj.parameters()) + [W], lr=lr)

    def logits(x):
        z = F.normalize(proj(x), dim=1)
        return z @ F.normalize(W, dim=1).T

    def view(x):
        return F.dropout(x + noise * sd * torch.randn_like(x), drop)

    g = torch.Generator().manual_seed(seed)
    for ep in range(epochs):
        tt = tau_t[0] + (tau_t[1] - tau_t[0]) * min(1.0, ep / warmup)
        perm = torch.randperm(len(X), generator=g)
        for i in range(0, len(X), batch):
            b = perm[i:i + batch]
            x, lab, ml = X[b], ylab[b], is_l[b]
            l1, l2 = logits(view(x)), logits(view(x))
            loss_sup = 0.0
            if ml.any():
                loss_sup = (F.cross_entropy(l1[ml] / tau_s, lab[ml]) +
                            F.cross_entropy(l2[ml] / tau_s, lab[ml])) / 2
            t1, t2 = F.softmax(l1.detach() / tt, 1), F.softmax(l2.detach() / tt, 1)
            s1, s2 = F.log_softmax(l1 / tau_s, 1), F.log_softmax(l2 / tau_s, 1)
            distill = -((t2 * s1).sum(1).mean() + (t1 * s2).sum(1).mean()) / 2
            pm = (F.softmax(l1 / tau_s, 1).mean(0) + F.softmax(l2 / tau_s, 1).mean(0)) / 2
            memax = (pm * torch.log(pm + 1e-8)).sum()            # = - entropia
            loss = sup_w * loss_sup + (1 - sup_w) * (distill + memax_w * memax)
            opt.zero_grad()
            loss.backward()
            opt.step()
    with torch.no_grad():
        pu = logits(torch.tensor(Xu, dtype=torch.float32)).argmax(1).numpy()
        pt = logits(torch.tensor(Xt, dtype=torch.float32)).argmax(1).numpy()

    def back(p):
        return np.where(p < C, classes[np.minimum(p, C - 1)], 10_000 + p)
    return back(pu), back(pt)


def exp_simgcd(data, seeds, seed0, n_known, n_new):
    rows = []
    for novelty in E.NOVELTIES:
        for seed in range(seed0, seed0 + seeds):
            for whiten in (False, True):
                D = split(data, n_known, n_new, novelty, seed, whiten)
                Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
                is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
                k_hat = E.estimate_k(Xl, yl, Xu, seed)
                for name, k_tot in (("SimGCD raso (K estimado)", k_hat),
                                    ("SimGCD raso (K oráculo)", n_known + n_new)):
                    t0 = time.time()
                    pu, pt = simgcd_shallow(Xl, yl, Xu, Xt, k_tot, seed)
                    a, o, n = do.gcd_acc(yu, pu, ~is_new_u)
                    ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
                    rows.append(dict(novelty=novelty, seed=seed, whiten=whiten, method=name,
                                     all=a, old=o, new=n, test_all=ta, test_old=to, test_new=tn,
                                     k_est=k_tot - n_known, secs=time.time() - t0))
            print(f"[simgcd {novelty} seed {seed}] ok", flush=True)
    return pd.DataFrame(rows)


# ----------------------------------------------------- 2. agrupamento alternativo
def group_rejected(method, dic, X, k, seed):
    """Agrupa X em k grupos com o método indicado (K̂ vem da dicotomia)."""
    if k < 2 or len(X) <= k:
        return np.zeros(len(X), int)
    if method == "espectral (P)":
        P = dic.proba_matrix(X, X)
        P = (P + P.T) / 2
        np.fill_diagonal(P, 1.0)
        return SpectralClustering(k, affinity="precomputed", random_state=seed,
                                  assign_labels="cluster_qr").fit_predict(P)
    if method == "Ward (espaço)":
        return AgglomerativeClustering(k, linkage="ward").fit_predict(X)
    if method == "k-means (espaço)":
        return KMeans(k, n_init=10, random_state=seed).fit_predict(X)
    raise ValueError(method)


ALT = ("espectral (P)", "Ward (espaço)", "k-means (espaço)")


def exp_cluster(data, seeds, seed0, n_known, n_new):
    rows = []
    for novelty in E.NOVELTIES:
        for seed in range(seed0, seed0 + seeds):
            D = split(data, n_known, n_new, novelty, seed)
            Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
            is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
            calib = do.calibrate(Xl, yl, CLF, seed)
            R = do.run_open_world(Xl, yl, Xu, CLF, seed, calib, noise=True)
            dic = R["dic"]
            # (a) descoberta com detecção oráculo
            Xn, yn = Xu[is_new_u], yu[is_new_u]
            lab = do.cluster_by_cut(dic, Xn, calib.cut)
            k = len(np.unique(lab))
            base = dict(novelty=novelty, seed=seed, k_hat_oracle=k)
            rows.append(dict(base, kind="descoberta", method="average linkage (P)",
                             acc=do.cluster_acc(yn, lab)[0]))
            for m in ALT:
                rows.append(dict(base, kind="descoberta", method=m,
                                 acc=do.cluster_acc(yn, group_rejected(m, dic, Xn, k, seed))[0]))
            # (b) ponta a ponta: mesmas rejeitadas e mesmo K̂, agrupamento trocado
            rej, pred0 = R["rejected"], R["pred"]
            k_e2e = R["n_new"]
            for m in ("average linkage (P)",) + ALT:
                pred = pred0.copy()
                if m != "average linkage (P)" and rej.any():
                    pred[rej] = yl.max() + 1 + group_rejected(m, dic, Xu[rej], k_e2e, seed)
                protos = np.vstack([Xl, Xu[rej]])
                proto_y = np.r_[yl, pred[rej]]
                pt = do.classify_with_bank(dic, Xt, protos, proto_y)
                a, o, n = do.gcd_acc(yu, pred, ~is_new_u)
                ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
                rows.append(dict(base, kind="ponta a ponta", method=m, k_est=k_e2e,
                                 all=a, new=n, test_all=ta, test_new=tn))
            print(f"[agrupamento {novelty} seed {seed}] ok", flush=True)
    return pd.DataFrame(rows)


# ------------------------------------------------------------ 3. ablação final
def sample_pairs_hard(X, y, neg_ratio=3, max_pos_per_class=45, rng=None, k_nn=10):
    """Como do.sample_pairs, mas metade dos negativos são difíceis: para uma âncora
    aleatória, um dos seus k_nn vizinhos mais próximos de OUTRA classe."""
    rng = rng or np.random.default_rng(0)
    idx_by_c = {c: np.flatnonzero(y == c) for c in np.unique(y)}
    pos = []
    for idx in idx_by_c.values():
        ii, jj = np.triu_indices(len(idx), 1)
        sel = rng.permutation(len(ii))[:max_pos_per_class]
        pos.append(np.c_[idx[ii[sel]], idx[jj[sel]]])
    pos = np.vstack(pos)
    n_neg = neg_ratio * len(pos)
    n_hard = n_neg // 2
    nn = NearestNeighbors(n_neighbors=min(len(y), k_nn * 4)).fit(X)
    nb = nn.kneighbors(X, return_distance=False)
    hard_nb = [row[y[row] != y[i]][:k_nn] for i, row in enumerate(nb)]
    anchors = rng.integers(0, len(y), 2 * n_hard)
    hard = [(a, rng.choice(hard_nb[a])) for a in anchors if len(hard_nb[a])][:n_hard]
    a = rng.integers(0, len(y), 2 * n_neg)
    b = rng.integers(0, len(y), 2 * n_neg)
    keep = y[a] != y[b]
    rand = np.c_[a[keep], b[keep]][:n_neg - len(hard)]
    P = np.vstack([pos, np.array(hard, int).reshape(-1, 2), rand])
    t = np.r_[np.ones(len(pos)), np.zeros(len(P) - len(pos))].astype(int)
    return do.pair_features(X[P[:, 0]], X[P[:, 1]]), t


def _ac_with(link):
    base = AgglomerativeClustering

    def ac(*a, **kw):
        if kw.get("metric") == "precomputed":
            kw["linkage"] = link
        return base(*a, **kw)
    return ac


# (fator, valor, mudanças); a primeira linha é o método
ABLATION = [
    ("padrão", "top3 / 3:1 / 64 / 25% / average", {}),
    ("agregação", "top1", dict(agg="top1")),
    ("agregação", "top5", dict(agg="top5")),
    ("agregação", "mean", dict(agg="mean")),
    ("negativos", "1:1", dict(neg=1)),
    ("negativos", "5:1", dict(neg=5)),
    ("negativos", "difíceis (50%)", dict(hard=True)),
    ("PCA", "128", dict(pca=128)),
    ("pseudo-novas", "15%", dict(frac=0.15)),
    ("pseudo-novas", "40%", dict(frac=0.40)),
    ("ligação", "single", dict(link="single")),
    ("ligação", "complete", dict(link="complete")),
]


@contextmanager
def variant(ch):
    saved = (do.AGG, do.NEG_RATIO, do.sample_pairs, do.AgglomerativeClustering)
    try:
        if "agg" in ch:
            do.AGG = ch["agg"]
        if "neg" in ch:
            do.NEG_RATIO = ch["neg"]
        if ch.get("hard"):
            do.sample_pairs = sample_pairs_hard
        if "link" in ch:
            do.AgglomerativeClustering = _ac_with(ch["link"])
        yield
    finally:
        do.AGG, do.NEG_RATIO, do.sample_pairs, do.AgglomerativeClustering = saved


def exp_ablation(data, seeds, seed0, n_known, n_new, factors=None):
    rows = []
    for factor, value, ch in ABLATION:
        if factors and factor not in factors and factor != "padrão":
            continue
        t0 = time.time()
        with variant(ch):
            for novelty in E.NOVELTIES:
                for seed in range(seed0, seed0 + seeds):
                    dim = data["X"].shape[1] if "X" in data else 10**6
                    pca = min(ch["pca"], dim) if "pca" in ch else None
                    D = split(data, n_known, n_new, novelty, seed, n_comp=pca)
                    Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
                    is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
                    calib = do.calibrate(Xl, yl, CLF, seed, frac=ch.get("frac", 0.25))
                    R = do.run_open_world(Xl, yl, Xu, CLF, seed, calib, noise=True)
                    Xn, yn = Xu[is_new_u], yu[is_new_u]
                    lab = do.cluster_by_cut(R["dic"], Xn, calib.cut)
                    pt = do.classify_with_bank(R["dic"], Xt, R["protos"], R["proto_y"])
                    a, o, n = do.gcd_acc(yu, R["pred"], ~is_new_u)
                    ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
                    rows.append(dict(factor=factor, value=value, novelty=novelty, seed=seed,
                                     auroc=roc_auc_score(~is_new_u, R["score"]),
                                     disc_acc=do.cluster_acc(yn, lab)[0], k_est=R["n_new"],
                                     k_true=n_new, all=a, new=n, test_all=ta, test_new=tn))
        print(f"[ablação {factor}={value}] {time.time() - t0:.0f}s", flush=True)
    return pd.DataFrame(rows)


# ------------------------------------------- 4. SimGCD raso com o K̂ da dicotomia
def exp_simgcd_khat(data, seeds, seed0, n_known, n_new, features,
                    src="results_v6", src_method="dicotomia-hgb + ruído", label="K da dicotomia"):
    """Combinação: a dicotomia conta as classes novas e a cabeça do SimGCD classifica.

    Lê o K̂ do método proposto em results_v6/<conjunto>/gcd.csv (mesma semente e
    cenário) e treina o SimGCD raso com n_known + K̂ protótipos, sem whitening
    (o pré-processamento do método). Nada é recalibrado.
    """
    g = pd.read_csv(Path(src) / Path(features).stem / "gcd.csv")
    g = g[g.method == src_method].set_index(["novelty", "seed"]).k_est
    rows = []
    for novelty in E.NOVELTIES:
        for seed in range(seed0, seed0 + seeds):
            D = split(data, n_known, n_new, novelty, seed)
            Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
            is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
            k_hat = int(g.loc[(novelty, seed)])
            pu, pt = simgcd_shallow(Xl, yl, Xu, Xt, n_known + k_hat, seed)
            a, o, n = do.gcd_acc(yu, pu, ~is_new_u)
            ta, to, tn = do.gcd_acc(yt, pt, is_old_t)
            rows.append(dict(novelty=novelty, seed=seed, whiten=False,
                             method=f"SimGCD raso ({label})", all=a, old=o, new=n,
                             test_all=ta, test_old=to, test_new=tn, k_est=k_hat))
        print(f"[simgcd {label} {novelty}] ok", flush=True)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True)
    ap.add_argument("--only", default="simgcd,cluster,ablation")
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--seed0", type=int, default=20)
    ap.add_argument("--factors", default=None,
                    help="restringe a ablação a alguns fatores, ex.: agregação,negativos")
    ap.add_argument("--out", default=None)
    ap.add_argument("--n-known", type=int, default=None, help="só para testes rápidos")
    ap.add_argument("--n-new", type=int, default=None, help="só para testes rápidos")
    args = ap.parse_args()
    data, n_known, n_new = setup(args.features, n_known_arg=args.n_known, n_new_arg=args.n_new)
    out = Path(args.out or Path("results_review") / Path(args.features).stem)
    out.mkdir(parents=True, exist_ok=True)
    only = set(args.only.split(","))
    print(f"{Path(args.features).stem}: {n_known} conhecidas, {n_new} novas, {E.NOVELTIES}, "
          f"sementes {args.seed0}-{args.seed0 + args.seeds - 1}, experimentos {sorted(only)}", flush=True)
    if "simgcd" in only:
        exp_simgcd(data, args.seeds, args.seed0, n_known, n_new).to_csv(out / "simgcd.csv", index=False)
    if "cluster" in only:
        exp_cluster(data, args.seeds, args.seed0, n_known, n_new).to_csv(out / "agrupamento.csv", index=False)
    if "simgcd_khat" in only:
        exp_simgcd_khat(data, args.seeds, args.seed0, n_known, n_new, args.features).to_csv(
            out / "simgcd_khat.csv", index=False)
    if "simgcd_keuclid" in only:
        exp_simgcd_khat(data, args.seeds, args.seed0, n_known, n_new, args.features,
                        src="results_v6_euclid", src_method="dicotomia-euclid + ruído",
                        label="K da distância fixa").to_csv(out / "simgcd_keuclid.csv", index=False)
    if "ablation" in only:
        fac = set(args.factors.split(",")) if args.factors else None
        exp_ablation(data, args.seeds, args.seed0, n_known, n_new, fac).to_csv(
            out / "ablacao_final.csv", index=False)
