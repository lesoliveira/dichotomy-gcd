"""Figura do passo de descoberta: dendrograma das amostras rejeitadas e matriz P(mesma).

    python fig_dendrogram.py                       # Omniglot-DINOv2, cenário far, semente 20
    python fig_dendrogram.py --novelty near --seed 21 --n-classes 8

Roda uma vez o pipeline (calibração, limiar out-of-fold, detecção) e guarda o necessário em
dendrograma_cache.npz; as execuções seguintes só redesenham (use --recompute para refazer).
Para a figura ficar legível, usa as amostras rejeitadas de n-classes classes novas sorteadas
e todas as conhecidas rejeitadas por engano. O agrupamento é refeito nesse subconjunto com o
corte calibrado, o que basta para ilustrar o procedimento.
"""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage
from scipy.spatial.distance import squareform

import dichotomy_owl as do
import experiments as E

plt.rcParams.update({"font.size": 8.5, "font.family": "serif", "pdf.fonttype": 42,
                     "axes.spines.top": False, "axes.spines.right": False})
PAL = ["#2a78d6", "#eb6834", "#1baf7a", "#b03a8c", "#7a4fc4", "#c9a227", "#1f4f8f", "#d6455d",
       "#4fb0c6", "#6b8e23"]
GREY = "#b9b8b2"


def compute(a):
    E.FEATS = Path(a.features)
    data = E.load()
    D = E.make_split(data, 100, 20, a.novelty, a.seed)
    Xl, yl, Xu, yu = D["Xl"], D["yl"], D["Xu"], D["yu"]
    calib = do.calibrate(Xl, yl, "hgb", a.seed)
    dic = do.Dichotomizer("hgb", a.seed).fit(Xl, yl)
    oof = do.oof_known_scores(Xl, yl, "hgb", a.seed)
    thr = float(np.quantile(oof, 1.0 - calib.known_tpr))
    S = do.class_scores(dic, Xu, Xl, yl, np.unique(yl)).max(1)
    rej = S < thr
    Xr, yr = Xu[rej], yu[rej]
    is_new = np.isin(yr, D["new"])
    rng = np.random.default_rng(a.seed)
    present = np.unique(yr[is_new])
    pick = rng.choice(present, min(a.n_classes, len(present)), replace=False)
    keep = np.isin(yr, pick) | ~is_new
    Xs, ys, ns = Xr[keep], yr[keep], is_new[keep]
    P = dic.proba_matrix(Xs, Xs)
    P = (P + P.T) / 2
    np.fill_diagonal(P, 1.0)
    np.savez(a.cache, P=P, y=ys, is_new=ns, cut=calib.cut, m=calib.min_size, thr=thr,
             n_rej=rej.sum(), n_rej_known=(~np.isin(yr, D["new"])).sum(), pick=pick)


def draw(a):
    c = np.load(a.cache)
    P, y, is_new, cut, m = c["P"], c["y"], c["is_new"], float(c["cut"]), int(c["m"])
    Dm = 1.0 - P
    np.fill_diagonal(Dm, 0.0)
    Z = linkage(squareform(Dm, checks=False), method="average")
    flat = fcluster(Z, t=1.0 - cut, criterion="distance")
    sizes = np.bincount(flat)
    kept = sizes[flat] >= m
    k_hat = len(np.unique(flat[kept]))
    cls = {k: PAL[i % len(PAL)] for i, k in enumerate(np.unique(y[is_new]))}
    true_col = [cls[v] if n else "#1f1f1d" for v, n in zip(y, is_new)]
    # cor de cada cluster descoberto = cor da classe majoritária (preto se for de conhecidas)
    kept_ids = {}
    for k in np.unique(flat[kept]):
        mem = flat == k
        vals, cnt = np.unique(np.where(is_new[mem], y[mem], -1), return_counts=True)
        maj = vals[cnt.argmax()]
        kept_ids[k] = "#1f1f1d" if maj == -1 else cls[maj]

    fig = plt.figure(figsize=(7.2, 4.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[2.15, 1], height_ratios=[1, 0.13],
                          wspace=0.22, hspace=0.04)
    ax = fig.add_subplot(gs[0, 0])
    dn = dendrogram(Z, ax=ax, no_labels=True, color_threshold=0, above_threshold_color="#5a5a55",
                    link_color_func=lambda k: "#5a5a55")
    ax.axhline(1.0 - cut, color="#d6455d", ls="--", lw=1.2)
    ax.text(ax.get_xlim()[0] + 4, 1.0 - cut + 0.015, f"cut at $1 - {cut:.2f}$", color="#d6455d",
            va="bottom", ha="left", fontsize=8,
            bbox=dict(facecolor="white", edgecolor="none", pad=1))
    ax.set_ylabel(r"average $1 - P(\mathrm{same})$")
    ax.set_title(f"(a) Dendrogram of the rejected samples: $\\hat K = {k_hat}$ clusters kept "
                 f"($m = {m}$)", loc="left", fontsize=9)
    ax.spines["bottom"].set_visible(False); ax.set_xticks([])
    order = dn["leaves"]
    xs = 5 + 10 * np.arange(len(order))
    axb = fig.add_subplot(gs[1, 0], sharex=ax)
    axb.scatter(xs, np.full(len(order), 1.0), c=[true_col[i] for i in order], s=14,
                marker="s", lw=0)
    axb.scatter(xs, np.zeros(len(order)),
                c=[kept_ids[flat[i]] if kept[i] else GREY for i in order], s=14, marker="s", lw=0)
    axb.set_yticks([1, 0]); axb.set_yticklabels(["true class", "discovered"], fontsize=7.5)
    axb.set_ylim(-0.6, 1.6); axb.set_xticks([])
    for s in axb.spines.values():
        s.set_visible(False)
    axb.tick_params(length=0)
    axh = fig.add_subplot(gs[0, 1])
    im = axh.imshow(P[np.ix_(order, order)], cmap="Blues", vmin=0, vmax=1, interpolation="nearest")
    axh.set_xticks([]); axh.set_yticks([])
    axh.set_title(r"(b) $P(\mathrm{same})$, dendrogram order", loc="left", fontsize=9)
    cb = fig.colorbar(im, ax=axh, fraction=0.046, pad=0.03); cb.ax.tick_params(labelsize=7)
    leg = fig.add_subplot(gs[1, 1]); leg.axis("off")
    leg.scatter([], [], c="#1f1f1d", marker="s", s=14, label="known (rejected by mistake)")
    leg.scatter([], [], c=GREY, marker="s", s=14, label=f"noise: cluster smaller than $m$")
    leg.scatter([], [], c=PAL[0], marker="s", s=14, label="colour of a novel class (discovered row:\nmajority class of the cluster)")
    leg.legend(frameon=False, fontsize=7, loc="center left", borderaxespad=0)
    fig.savefig(a.out + ".pdf", bbox_inches="tight")
    fig.savefig(a.out + ".png", dpi=180, bbox_inches="tight")
    print(f"{len(y)} amostras ({is_new.sum()} novas de {len(np.unique(y[is_new]))} classes, "
          f"{(~is_new).sum()} conhecidas rejeitadas), corte {cut:.2f}, m = {m}, "
          f"K̂ no subconjunto = {k_hat}; total rejeitadas na execução = {int(c['n_rej'])}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", default="omniglot_dinov2.npz")
    ap.add_argument("--novelty", default="far")
    ap.add_argument("--seed", type=int, default=20)
    ap.add_argument("--n-classes", type=int, default=8)
    ap.add_argument("--cache", default="dendrograma_cache.npz")
    ap.add_argument("--out", default="figures/dendrogram")
    ap.add_argument("--recompute", action="store_true")
    a = ap.parse_args()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    if a.recompute or not Path(a.cache).exists():
        compute(a)
    draw(a)
