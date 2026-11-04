"""Ablação da dissimilaridade aprendida: mesmo pipeline com o dichotomizer (boosting)
vs. com distância euclidiana fixa calibrada (EuclidLogit). Wilcoxon pareado por
(conjunto, cenário, semente), por conjunto e agrupado.

    python compare_ablation.py results_v6 results_v6_euclid
"""
import sys
from pathlib import Path

import pandas as pd
from scipy.stats import wilcoxon

A, B = Path(sys.argv[1]), Path(sys.argv[2])
K = ["ds", "novelty", "seed"]


def load(kind):
    out = []
    for d in sorted(p.name for p in B.iterdir() if p.is_dir()):
        for root in (A, B):
            f = root / d / f"{kind}.csv"
            if f.exists():
                x = pd.read_csv(f); x["ds"] = d; out.append(x)
    return pd.concat(out).drop_duplicates(subset=K + ["method"])


def test(df, a, b, col, dss=None):
    if dss is not None:
        df = df[df.ds.isin(dss)]
    x = df[df.method == a].set_index(K)[col]; y = df[df.method == b].set_index(K)[col]
    d = (x - y).dropna()
    if d.empty:
        return None
    p = wilcoxon(d).pvalue if (d != 0).any() else 1.0
    return dict(A=a, B=b, métrica=col, n=len(d), dif=round(d.mean(), 3),
                A_vence=f"{int((d > 0).sum())}/{len(d)}", p=round(p, 4))


g, s, t = load("gcd"), load("descoberta"), load("deteccao")
kt = g[g.method == "SS-kmeans (K oráculo)"].set_index(K).k_est.rename("k_true")
g = g.join(kt, on=K); g["k_err"] = (g.k_est - g.k_true).abs()
rows = []
groups = [("todos", None)] + [(d, [d]) for d in sorted(g.ds.unique())]
for name, dss in groups:
    for col in ("test_all", "test_new", "all", "new", "k_err"):
        r = test(g, "dicotomia-hgb + ruído", "dicotomia-euclid + ruído", col, dss)
        if r: rows.append(dict(grupo=name, **r))
    r = test(t, "dicotomia-hgb", "dicotomia-euclid", "auroc", dss)
    if r: rows.append(dict(grupo=name, **r))
    r = test(s, "dicotomia-hgb (K auto)", "dicotomia-euclid (K auto)", "acc", dss)
    if r: rows.append(dict(grupo=name, **r))
    r = test(g, "dicotomia-euclid + ruído", "SS-kmeans (K estimado)", "test_all", dss)
    if r: rows.append(dict(grupo=name, **r))
out = pd.DataFrame(rows)
txt = ("# Ablação: dissimilaridade aprendida (hgb) vs. distância euclidiana calibrada\n\n"
       "Para k_err, menor é melhor (diferença negativa favorece A).\n\n" + out.to_markdown(index=False))
(B / "ablacao_dissimilaridade.md").write_text(txt)
print(txt)
