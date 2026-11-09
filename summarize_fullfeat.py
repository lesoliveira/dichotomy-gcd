"""Summary of baselines_fullfeat.py.

    python summarize_fullfeat.py      -> results_fullfeat/fullfeat.md

Compares, over the paired runs available, SimGCD with the K̂ of the dichotomy against
SimGCD with the searched K and with the true K, on full features, and against the 64-PCA
numbers of the paper (results_review/<set>/simgcd*.csv, baselines with their best
whitening). The strictest comparison gives each baseline the better of its 64-PCA and
full-feature runs, per setting.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

SETS = ["omniglot_dinov2", "omniglot_hog", "cub_dinov2", "ts_ShapesAll",
        "ts_NonInvasiveFetalECGThorax1", "ts_Crop", "ts_SwedishLeaf"]
KEY = ["ds", "novelty", "seed"]
EST, ORA, OURS = "SimGCD raso (K estimado)", "SimGCD raso (K oráculo)", "SimGCD raso (K da dicotomia)"
SSE = "SS-kmeans (K estimado)"


def best_whiten(x):
    if "whiten" in x and x.whiten.nunique() > 1:
        return x[x.whiten == x.groupby("whiten").test_all.mean().idxmax()]
    return x


rows = []
for d in SETS:
    f = Path("results_fullfeat") / d / "full.csv"
    if not f.exists():
        continue
    full = pd.read_csv(f).assign(ds=d, prep="full")
    rows.append(full)
    s = pd.read_csv(Path("results_review") / d / "simgcd.csv")
    for m in (EST, ORA):
        rows.append(best_whiten(s[s.method == m]).assign(ds=d, prep="pca64"))
    h = pd.read_csv(Path("results_review") / d / "simgcd_khat.csv")
    rows.append(h.assign(ds=d, prep="pca64", method=OURS))
X = pd.concat(rows)[KEY + ["prep", "method", "k_est", "test_all", "test_new"]]
have = set(map(tuple, X[(X.prep == "full") & (X.method == OURS)][KEY].values))
X = X[[tuple(r) in have for r in X[KEY].values]]

# best of 64-PCA and full features for each baseline, chosen per setting by mean accuracy
best = []
for (d, m), g in X[X.method.isin([EST, ORA])].groupby(["ds", "method"]):
    p = g.groupby("prep").test_all.mean().idxmax()
    best.append(g[g.prep == p].assign(prep="best"))
X = pd.concat([X] + best)
X["name"] = X.method + " [" + X.prep + "]"

txt = [f"# Baselines on full features ({len(have)} paired runs)\n"]
t = X.groupby(["ds", "name"]).test_all.mean().mul(100).round(1).unstack("name")
txt += ["## Test accuracy, all classes (%)\n", t.to_markdown(), "\n"]
p = X.groupby("name")[["test_all", "test_new"]].mean().mul(100).round(2)
txt += ["## Pooled\n", p.to_markdown(), "\n"]


def paired(a, b, col="test_all"):
    A = X[X.name == a].set_index(KEY)[col]
    B = X[X.name == b].set_index(KEY)[col]
    d = (A - B).dropna()
    p = wilcoxon(d).pvalue if (d != 0).any() and len(d) > 5 else np.nan
    return dict(a=a, b=b, metric=col, n=len(d), diff_points=round(100 * d.mean(), 2),
                a_wins=int((d > 0).sum()), b_wins=int((d < 0).sum()), p=p)


tests = [paired(f"{OURS} [full]", f"{EST} [full]"),
         paired(f"{OURS} [full]", f"{EST} [full]", "test_new"),
         paired(f"{OURS} [pca64]", f"{EST} [best]"),
         paired(f"{OURS} [full]", f"{EST} [best]"),
         paired(f"{OURS} [full]", f"{ORA} [full]"),
         paired(f"{OURS} [full]", f"{OURS} [pca64]"),
         paired(f"{EST} [full]", f"{EST} [pca64]")]
txt += ["## Paired tests (differences in points)\n", pd.DataFrame(tests).to_markdown(index=False, floatfmt=".4g"), "\n"]
F = pd.concat([pd.read_csv(Path("results_fullfeat") / d / "full.csv").assign(ds=d)
               for d in SETS if (Path("results_fullfeat") / d / "full.csv").exists()])
F["k_err"] = (F.k_est - F.k_true).abs()
t = F[F.method.isin([EST, OURS])].groupby(["ds", "method"]).k_err.mean().round(1).unstack("method")
txt += ["## |K̂ − K|: search on full features vs. dichotomy (64-PCA)\n", t.to_markdown(), "\n"]
Path("results_fullfeat/fullfeat.md").write_text("\n".join(txt))
print("\n".join(txt))
