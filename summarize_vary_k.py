"""Table and figure for vary_k.py.

    python summarize_vary_k.py            -> results_vary_k/vary_k.md, figures/vary_k.pdf

For the baselines that were run with and without whitening (SS-k-means and SimGCD with
the Vaze et al. estimate), each setting and K keeps the better of the two by mean test
accuracy, as in the paper. Means are over seeds and, for Omniglot and CUB, both scenarios.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

plt.rcParams.update({"font.size": 9, "font.family": "serif", "axes.spines.top": False,
                     "axes.spines.right": False, "pdf.fonttype": 42})
B, O, G, P, GR = "#2a78d6", "#eb6834", "#1baf7a", "#7a4fc4", "#8a8a85"
ROOT = Path("results_vary_k")
SETS = [("omniglot_dinov2", "Omniglot · DINOv2"), ("omniglot_hog", "Omniglot · HOG"),
        ("cub_dinov2", "CUB · DINOv2"), ("ts_ShapesAll", "ShapesAll · MiniRocket")]
OURS = "dicotomia-hgb + ruído"
CORR = "dicotomia-hgb corrigida"
METHODS = [(OURS, "Dichotomy (ours)", B, "-o"),
           (CORR, "Dichotomy, corrected count", "#8fb8ea", "-.o"),
           ("dicotomia-euclid + ruído", "Same pipeline, fixed distance", O, "--s"),
           ("SS-kmeans (K estimado)", "SS-k-means, estimated K", G, ":^"),
           ("SimGCD raso (K da dicotomia)", "SimGCD, K from dichotomy", P, "-D"),
           ("SimGCD raso (K estimado)", "SimGCD, estimated K", GR, ":v"),
           ("SimGCD raso (K oráculo)", "SimGCD, true K", "#1f1f1d", "-.x")]


def load(d):
    f = ROOT / d / "vary_k.csv"
    if not f.exists():
        return None
    x = pd.read_csv(f)
    fc = ROOT / d / "vary_k_corr.csv"
    if fc.exists():                      # K̂ with the bias correction (vary_k_corr.py)
        c = pd.read_csv(fc)
        c = c[(c.method == "dicotomia-hgb") & (c["corr"] == "rate")].copy()
        c["method"], c["whiten"] = CORR, False
        x = pd.concat([x, c[["novelty", "seed", "k_true", "method", "whiten", "k_est", "test_all",
                             "test_old", "test_new"]]])
    x["k_err"] = (x.k_est - x.k_true).abs()
    # best of whitened / non-whitened for the baselines that have both
    keep = []
    for (m, k), g in x.groupby(["method", "k_true"]):
        if g.whiten.nunique() > 1:
            w = g.groupby("whiten").test_all.mean().idxmax()
            g = g[g.whiten == w]
        keep.append(g)
    return pd.concat(keep)


def main():
    txt = ["# Sensitivity to the number of novel classes K\n",
           "Mean over seeds (and near/far for Omniglot and CUB). Accuracy in %.\n"]
    data = {d: load(d) for d, _ in SETS}
    for d, name in SETS:
        x = data[d]
        if x is None:
            continue
        g = x.groupby(["method", "k_true"])
        t = pd.DataFrame({"K̂": g.k_est.mean().round(1), "|K̂−K|": g.k_err.mean().round(1),
                          "test all": (100 * g.test_all.mean()).round(1),
                          "test new": (100 * g.test_new.mean()).round(1),
                          "AUROC": (100 * g.auroc.mean()).round(1) if "auroc" in x else np.nan})
        txt += [f"\n## {name}\n", t.to_markdown(), "\n"]
        # paired test: ours vs SS-k-means on |K̂ − K| and on test accuracy, per K
        rows = []
        for k in sorted(x.k_true.unique()):
            a = x[(x.method == OURS) & (x.k_true == k)].set_index(["novelty", "seed"])
            for other in ("SS-kmeans (K estimado)", "dicotomia-euclid + ruído"):
                b = x[(x.method == other) & (x.k_true == k)].set_index(["novelty", "seed"])
                for m in ("k_err", "test_all"):
                    dd = (a[m] - b[m]).dropna()
                    p = wilcoxon(dd).pvalue if (dd != 0).any() and len(dd) > 5 else np.nan
                    rows.append(dict(K=k, vs=other, metric=m, ours_minus_other=round(dd.mean(), 3),
                                     n=len(dd), p=p))
        txt += ["Ours minus other (paired by scenario and seed):\n",
                pd.DataFrame(rows).to_markdown(index=False, floatfmt=".4g"), "\n"]
    (ROOT / "vary_k.md").write_text("\n".join(txt))
    print("\n".join(txt))

    avail = [(d, n) for d, n in SETS if data[d] is not None]
    fig, axs = plt.subplots(2, len(avail), figsize=(1.9 * len(avail) + 0.6, 4.6), squeeze=False)
    for j, (d, name) in enumerate(avail):
        x = data[d]
        ks = sorted(x.k_true.unique())
        ax = axs[0, j]
        ax.plot(ks, ks, color="#d0cfca", lw=1, zorder=0)
        for m, lab, c, st in METHODS[:4]:
            s = x[x.method == m].groupby("k_true").k_est
            ax.errorbar(s.mean().index, s.mean().values, yerr=s.std().values, fmt=st, color=c,
                        lw=1.4, ms=3.5, capsize=2, label=lab)
        ax.set_title(name, loc="left", fontsize=8.5)
        ax.set_xticks(ks)
        ax = axs[1, j]
        for m, lab, c, st in [M for M in METHODS if M[0] != CORR]:
            s = 100 * x[x.method == m].groupby("k_true").test_all.mean()
            ax.plot(s.index, s.values, st, color=c, lw=1.4, ms=3.5, label=lab)
        ax.set_xticks(ks)
        for a in axs[:, j]:
            a.grid(axis="y", color="#e6e5e0", lw=.7)
    axs[0, 0].set_ylabel(r"estimated $\hat K$")
    axs[1, 0].set_ylabel("test accuracy, all classes (%)")
    h0, l0 = axs[0, 0].get_legend_handles_labels()
    h1, l1 = axs[1, 0].get_legend_handles_labels()
    seen = dict(zip(l1, h1))
    seen.update({l: h for l, h in zip(l0, h0) if l not in seen})
    order = [lab for _, lab, _, _ in METHODS if lab in seen]
    fig.supxlabel("true number of novel classes $K$", fontsize=9, y=0.1)
    fig.legend([seen[l] for l in order], order, loc="lower center", ncol=4, frameon=False,
               fontsize=7.5)
    fig.tight_layout(rect=(0, 0.1, 1, 1))
    Path("figures").mkdir(exist_ok=True)
    fig.savefig("figures/vary_k.pdf"); fig.savefig("figures/vary_k.png", dpi=180)
    print("figures/vary_k.pdf written")


if __name__ == "__main__":
    main()
