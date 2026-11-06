"""Summary of vary_k_corr.py, joined with the baselines of vary_k.py.

    python summarize_vary_k_corr.py      -> results_vary_k/vary_k_corr.md
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

ROOT = Path("results_vary_k")
SETS = ["omniglot_dinov2", "omniglot_hog", "cub_dinov2", "ts_ShapesAll"]
KEY = ["set", "novelty", "seed", "k_true"]


def load():
    C, V = [], []
    for d in SETS:
        if (ROOT / d / "vary_k_corr.csv").exists():
            C.append(pd.read_csv(ROOT / d / "vary_k_corr.csv").assign(set=d))
            V.append(pd.read_csv(ROOT / d / "vary_k.csv").assign(set=d))
    C, V = pd.concat(C), pd.concat(V)
    keep = []
    for _, g in V.groupby(["set", "method", "k_true"]):     # best of whitening, as in the paper
        if g.whiten.nunique() > 1:
            g = g[g.whiten == g.groupby("whiten").test_all.mean().idxmax()]
        keep.append(g)
    V = pd.concat(keep)
    C["name"] = C.method + " [" + C["corr"] + "]"
    V["name"] = V.method
    X = pd.concat([C,
                   V[V.method.isin(["SS-kmeans (K estimado)", "SimGCD raso (K estimado)",
                                    "SimGCD raso (K da dicotomia)", "SimGCD raso (K oráculo)"])]])
    X["err"] = (X.k_est - X.k_true).abs()
    X["bias"] = X.k_est - X.k_true
    return X


def paired(X, a, b, col):
    A = X[X.name == a].set_index(KEY)[col]
    B = X[X.name == b].set_index(KEY)[col]
    d = (A - B).dropna()
    p = wilcoxon(d).pvalue if (d != 0).any() and len(d) > 5 else np.nan
    return dict(a=a, b=b, metric=col, mean_diff=round(d.mean(), 3), a_better=int((d < 0).sum() if col == "err" else (d > 0).sum()),
                b_better=int((d > 0).sum() if col == "err" else (d < 0).sum()), n=len(d), p=p)


def main():
    X = load()
    txt = ["# Bias correction of K̂\n"]
    for c in ("rate", "pseudo", "binom"):
        H = X[X.name == f"dicotomia-hgb [{c}]"]
        r = np.corrcoef(H.k0, H.true_spur)[0, 1]
        txt.append(f"Offset {c}: mean K̂₀ {H.k0.mean():.1f} vs true known-dominated clusters "
                   f"{H.true_spur.mean():.1f}, r = {r:.2f}\n")
    for sub, lab in ((X[X.k_true > 0], "K > 0"), (X[X.k_true == 0], "K = 0")):
        g = sub.groupby(["set", "name"])
        t = pd.DataFrame({"K̂−K": g.bias.mean().round(1), "|K̂−K|": g.err.mean().round(1),
                          "test all %": (100 * g.test_all.mean()).round(1)})
        txt += [f"\n## Per setting, {lab}\n", t.to_markdown(), "\n"]
        g = sub.groupby("name")
        t = pd.DataFrame({"K̂−K": g.bias.mean().round(1), "|K̂−K|": g.err.mean().round(1),
                          "test all %": (100 * g.test_all.mean()).round(1)})
        txt += [f"\n## Pooled, {lab}\n", t.to_markdown(), "\n"]
    P = X[X.k_true > 0]
    rows = []
    for c in ("rate", "pseudo", "binom"):
        rows += [paired(P, f"dicotomia-hgb [{c}]", "dicotomia-hgb [none]", "err"),
                 paired(P, f"dicotomia-hgb [{c}]", "dicotomia-hgb [none]", "test_all"),
                 paired(P, f"dicotomia-hgb [{c}]", "SS-kmeans (K estimado)", "err"),
                 paired(P, f"dicotomia-hgb [{c}]", f"dicotomia-euclid [{c}]", "err"),
                 paired(P, f"SimGCD raso (K da dicotomia) [{c}]", "SimGCD raso (K da dicotomia)", "test_all"),
                 paired(P, f"SimGCD raso (K da dicotomia) [{c}]", "SimGCD raso (K estimado)", "test_all")]
    txt += ["\n## Paired tests, K > 0 (a vs b)\n", pd.DataFrame(rows).to_markdown(index=False, floatfmt=".4g"), "\n"]
    g = P.groupby(["k_true", "name"])
    t = pd.DataFrame({"K̂": g.k_est.mean().round(1), "|K̂−K|": g.err.mean().round(1)}).unstack("name")
    txt += ["\n## By K (pooled over settings)\n", t.to_markdown(), "\n"]
    (ROOT / "vary_k_corr.md").write_text("\n".join(txt))
    print("\n".join(txt))


if __name__ == "__main__":
    main()
