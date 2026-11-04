"""Paper figures computed from the result files.

    python make_figures.py            -> figures/rq1.pdf, figures/scale.pdf

rq1.pdf    transfer of the learned similarity (pairwise AUC between novel classes vs. number
           of known classes), from results_v6/*/transferencia_hgb.csv. Omniglot and CUB use
           the far scenario (unseen alphabets, SSB Easy).
scale.pdf  test accuracy on all classes vs. number of known classes for the prototype-based
           pipeline, the same pipeline with a fixed distance, and semi-supervised k-means with
           estimated K (best of the whitened and non-whitened runs, as in the paper).
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 9, "font.family": "serif", "axes.spines.top": False,
                     "axes.spines.right": False, "pdf.fonttype": 42})
B, O, G, GR = "#2a78d6", "#eb6834", "#1baf7a", "#8a8a85"
OUT = Path("figures")

RQ1 = [("omniglot_dinov2", "Omniglot · DINOv2", B, "o", "far"),
       ("omniglot_hog", "Omniglot · HOG", "#1f4f8f", "s", "far"),
       ("cub_dinov2", "CUB · DINOv2", "#7a4fc4", "P", "far"),
       ("ts_ShapesAll", "ShapesAll", O, "^", "random"),
       ("ts_NonInvasiveFetalECGThorax1", "ECG fetal", G, "D", "random"),
       ("ts_Crop", "Crop", "#b03a8c", "v", "random"),
       ("ts_SwedishLeaf", "SwedishLeaf", GR, "p", "random")]


def fig_rq1():
    fig, ax = plt.subplots(figsize=(7.2, 3.0))
    ticks = set()
    for d, name, c, m, nov in RQ1:
        f = Path("results_v6") / d / "transferencia_hgb.csv"
        if not f.exists():
            continue
        t = pd.read_csv(f)
        s = t[t.novelty == nov].groupby("n_known").pair_auc_new.mean()
        ax.plot(s.index, s.values, "-", marker=m, color=c, lw=1.5, ms=4, label=name)
        ticks |= set(s.index)
    ax.set_xscale("log")
    t = sorted(ticks)
    ax.set_xticks(t); ax.set_xticklabels(t); ax.minorticks_off()
    ax.set_xlabel("known classes used to train the dichotomizer (log scale)")
    ax.set_ylabel("pairwise AUC on novel classes")
    ax.grid(axis="y", color="#e6e5e0", lw=.7)
    ax.legend(frameon=False, fontsize=7.5, ncol=2, loc="lower right")
    fig.tight_layout(); fig.savefig(OUT / "rq1.pdf")


def scale_curve(path, method):
    if not Path(path).exists():
        return None
    x = pd.read_csv(path)
    return x[(x.kind == "gcd") & (x.method == method)].groupby("n_known").test_all.mean()


def fig_scale():
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.7))
    for ax, (d, title) in zip(axs, [("omniglot_dinov2", "(a) Omniglot · DINOv2"),
                                    ("ts_ShapesAll", "(b) ShapesAll · MiniRocket")]):
        ours = scale_curve(f"results_v6/{d}/escala.csv", "dicotomia-hgb + ruído")
        fixed = scale_curve(f"results_v6_euclid/{d}/escala.csv", "dicotomia-euclid + ruído")
        g6 = scale_curve(f"results_v6/{d}/escala.csv", "SS-kmeans (K estimado)")
        g5 = scale_curve(f"results_v5/{d}/escala.csv", "SS-kmeans (K estimado)")
        gcd = pd.concat([g6, g5], axis=1).max(axis=1) if g5 is not None else g6
        for s, lab, c, st in [(ours, "Dichotomy (ours)", B, "-o"),
                              (fixed, "Same pipeline, fixed distance", O, "--s"),
                              (gcd, "SS-k-means, estimated K", G, ":^")]:
            if s is not None:
                ax.plot(s.index, s.values, st, color=c, lw=1.6, ms=4, label=lab)
        ax.set_xscale("log"); ax.set_xticks(ours.index); ax.set_xticklabels(ours.index)
        ax.minorticks_off(); ax.set_xlabel("known classes (log scale)")
        ax.set_title(title, loc="left", fontsize=9); ax.grid(axis="y", color="#e6e5e0", lw=.7)
    axs[0].set_ylabel("test accuracy, all classes")
    axs[0].legend(frameon=False, fontsize=7.5, loc="lower right")
    fig.tight_layout(); fig.savefig(OUT / "scale.pdf")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    fig_rq1()
    fig_scale()
    print("figures/rq1.pdf and figures/scale.pdf written")
