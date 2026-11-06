"""Main result with the bias-corrected K̂, default K of each setting (50 paired runs).

    python khat_corr_tables.py     -> results_vary_k/khat_corr.md

Rows of vary_k_corr.csv at the default K are joined with results_review (SimGCD with the
estimated K, best of whitening as in the paper, and with the true K).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

DEF = {"omniglot_dinov2": 20, "omniglot_hog": 20, "cub_dinov2": 20, "ts_ShapesAll": 20,
       "ts_NonInvasiveFetalECGThorax1": 14, "ts_Crop": 8, "ts_SwedishLeaf": 5}
KEY = ["ds", "novelty", "seed"]
CORR = "rate"


def best_whiten(x):
    w = x.groupby("whiten").test_all.mean().idxmax()
    return x[x.whiten == w]


rows = []
for d, k in DEF.items():
    f = Path("results_vary_k") / d / "vary_k_corr.csv"
    if not f.exists():
        print("missing", f)
        continue
    c = pd.read_csv(f)
    c = c[c.k_true == k]
    s = pd.read_csv(Path("results_review") / d / "simgcd.csv")
    for name, x in [("dichotomy K̂ raw", c[(c.method == "dicotomia-hgb") & (c["corr"] == "none")]),
                    ("dichotomy K̂ corrected", c[(c.method == "dicotomia-hgb") & (c["corr"] == CORR)]),
                    ("fixed distance K̂ raw", c[(c.method == "dicotomia-euclid") & (c["corr"] == "none")]),
                    ("fixed distance K̂ corrected", c[(c.method == "dicotomia-euclid") & (c["corr"] == CORR)]),
                    ("SimGCD, K̂ corrected", c[(c.method == "SimGCD raso (K da dicotomia)") & (c["corr"] == CORR)]),
                    ("SimGCD, estimated K", best_whiten(s[s.method == "SimGCD raso (K estimado)"])),
                    ("SimGCD, true K", best_whiten(s[s.method == "SimGCD raso (K oráculo)"]))]:
        x = x.assign(ds=d, name=name, k_true=k)
        rows.append(x)
h = pd.concat([pd.read_csv(Path("results_review") / d / "simgcd_khat.csv").assign(ds=d, k_true=k)
               for d, k in DEF.items() if (Path("results_review") / d / "simgcd_khat.csv").exists()])
rows.append(h.assign(name="SimGCD, K̂ raw"))
X = pd.concat(rows)
X.loc[X.name.isin(["SimGCD, estimated K"]) & X.k_est.isna(), "k_est"] = np.nan
X["k_err"] = (X.k_est - X.k_true).abs()
# keep only the runs where the corrected K̂ exists, so every row averages the same runs
have = set(map(tuple, X[X.name == "SimGCD, K̂ corrected"][KEY].values))
X = X[[tuple(r) in have for r in X[KEY].values]]

txt = ["# Main result with the corrected K̂\n", f"Correction: {CORR}. Default K of each setting.\n"]
t = X.groupby(["ds", "name"])[["k_err", "test_all", "test_new"]].mean()
t[["test_all", "test_new"]] *= 100
txt += ["## Per setting\n", t.round(1).unstack("name").to_markdown(), "\n"]
p = X.groupby("name")[["k_err", "test_all", "test_new"]].mean()
p[["test_all", "test_new"]] *= 100
txt += [f"## Pooled ({len(have)} runs)\n", p.round(2).to_markdown(), "\n"]


def paired(a, b, col):
    A = X[X.name == a].set_index(KEY)[col]
    B = X[X.name == b].set_index(KEY)[col]
    d = (A - B).dropna()
    better = (d < 0).sum() if col == "k_err" else (d > 0).sum()
    return dict(a=a, b=b, metric=col, n=len(d), diff=round(d.mean() * (1 if col == "k_err" else 100), 2),
                a_better=f"{better}/{len(d)}", p=wilcoxon(d).pvalue if (d != 0).any() else 1.0)


tests = [paired("dichotomy K̂ corrected", "dichotomy K̂ raw", "k_err"),
         paired("dichotomy K̂ corrected", "fixed distance K̂ corrected", "k_err"),
         paired("SimGCD, K̂ corrected", "SimGCD, K̂ raw", "test_all"),
         paired("SimGCD, K̂ corrected", "SimGCD, estimated K", "test_all"),
         paired("SimGCD, K̂ corrected", "SimGCD, true K", "test_all"),
         paired("SimGCD, K̂ corrected", "SimGCD, estimated K", "test_new")]
txt += ["## Paired tests (accuracy differences in points)\n",
        pd.DataFrame(tests).to_markdown(index=False, floatfmt=".4g"), "\n"]
Path("results_vary_k/khat_corr.md").write_text("\n".join(txt))
print("\n".join(txt))
