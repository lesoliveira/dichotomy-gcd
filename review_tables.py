"""Tabelas dos experimentos da revisão.

    python review_tables.py            -> results_review/revisao.md

Usa results_review/<conjunto>/{simgcd,agrupamento,ablacao_final}.csv e, para o
método proposto, results_v6/<conjunto>/gcd.csv. Testes de Wilcoxon pareados por
(conjunto, cenário, semente). No SimGCD, o baseline recebe o melhor de com e sem
whitening em cada conjunto e métrica (o mesmo critério conservador do artigo).
"""
from pathlib import Path

import pandas as pd
from scipy.stats import wilcoxon

ALL = ["omniglot_dinov2", "omniglot_hog", "cub_dinov2", "ts_ShapesAll",
       "ts_NonInvasiveFetalECGThorax1", "ts_Crop", "ts_SwedishLeaf"]
K = ["ds", "novelty", "seed"]
OURS = "dicotomia-hgb + ruído"
R = Path("results_review")


def load(name):
    out = []
    for d in ALL:
        f = R / d / name
        if f.exists():
            x = pd.read_csv(f)
            x["ds"] = d
            out.append(x)
    return pd.concat(out) if out else None


def test(diff, lower_better=False):
    d = diff.dropna()
    if d.empty:
        return dict(n=0)
    p = wilcoxon(d).pvalue if (d != 0).any() else 1.0
    wins = (d < 0).sum() if lower_better else (d > 0).sum()
    return dict(n=len(d), dif=round(d.mean(), 3), a_favor=f"{int(wins)}/{len(d)}", p=round(p, 4))


md = ["# Experimentos da revisão (sementes 20-24)\n"]

# ------------------------------------------------------------------ SimGCD raso
S = load("simgcd.csv")
if S is not None:
    ours = []
    for d in S.ds.unique():
        x = pd.read_csv(Path("results_v6") / d / "gcd.csv")
        x = x[x.method == OURS]
        x["ds"] = d
        ours.append(x)
    O = pd.concat(ours).set_index(K)
    md.append("## 1. Proposto vs. SimGCD raso nas mesmas features fixas\n")
    rows, per = [], []
    for m in S.method.unique():
        for col in ("test_all", "test_new", "all", "new"):
            best = []
            for d in S.ds.unique():
                x = S[(S.method == m) & (S.ds == d)]
                w = x.groupby("whiten")[col].mean().idxmax()
                best.append(x[x.whiten == w])
            B = pd.concat(best).set_index(K)[col]
            rows.append(dict(comparação=f"proposto − {m}", métrica=col, **test(O[col] - B)))
            for d in S.ds.unique():
                per.append(dict(método=m, métrica=col, ds=d, valor=B.xs(d, level="ds").mean(),
                                proposto=O[col].xs(d, level="ds").mean()))
    md += [pd.DataFrame(rows).to_markdown(index=False), "\n### Médias por conjunto\n",
           pd.DataFrame(per).pivot_table(index=["método", "métrica"], columns="ds",
                                         values=["valor", "proposto"]).round(3).to_markdown(), "\n"]

# --------------------------------------------------------- agrupamento alternativo
A = load("agrupamento.csv")
if A is not None:
    md.append("## 2. Agrupamento a partir de P(mesma classe), mesmo K̂\n")
    for kind, cols in (("descoberta", ["acc"]), ("ponta a ponta", ["test_all", "test_new", "new"])):
        x = A[A.kind == kind]
        base = x[x.method == "average linkage (P)"].set_index(K)
        rows = []
        for m in x.method.unique():
            if m == "average linkage (P)":
                continue
            y = x[x.method == m].set_index(K)
            for col in cols:
                rows.append(dict(comparação=f"{m} − average linkage", métrica=col,
                                 **test(y[col] - base[col])))
        md += [f"### {kind}\n", pd.DataFrame(rows).to_markdown(index=False), "\n",
               x.groupby(["method", "ds"])[cols].mean().unstack("ds").round(3).to_markdown(), "\n"]

# ------------------------------------------------------------------ ablação final
B = load("ablacao_final.csv")
if B is not None:
    md.append("## 3. Sensibilidade no protocolo final (diferença para o padrão)\n")
    base = B[B.factor == "padrão"].set_index(K)
    B["k_err"] = (B.k_est - B.k_true).abs()
    base = B[B.factor == "padrão"].set_index(K)
    rows = []
    for (f, v), y in B[B.factor != "padrão"].groupby(["factor", "value"], sort=False):
        y = y.set_index(K)
        for col in ("test_all", "test_new", "auroc", "disc_acc", "k_err"):
            rows.append(dict(fator=f, valor=v, métrica=col,
                             **test(y[col] - base[col], lower_better=(col == "k_err"))))
    md += [pd.DataFrame(rows).to_markdown(index=False), "\n### Médias\n",
           B.groupby(["factor", "value"], sort=False)[["test_all", "test_new", "auroc",
                                                         "disc_acc", "k_err"]].mean().round(3)
           .to_markdown(), "\n"]

# ------------------------------------------------- SimGCD com o K̂ da dicotomia
H = load("simgcd_khat.csv")
if H is not None and S is not None:
    md.append("## 4. SimGCD raso com o K̂ da dicotomia\n")
    Hh = H.set_index(K)
    rows = []
    for col in ("test_all", "test_new", "all", "new"):
        rows.append(dict(comparação="SimGCD (K da dicotomia) − proposto", métrica=col,
                         **test(Hh[col] - O[col])))
        for m in ("SimGCD raso (K estimado)", "SimGCD raso (K oráculo)"):
            best = []
            for d in S.ds.unique():
                x = S[(S.method == m) & (S.ds == d)]
                w = x.groupby("whiten")[col].mean().idxmax()
                best.append(x[x.whiten == w])
            Bm = pd.concat(best).set_index(K)[col]
            rows.append(dict(comparação=f"SimGCD (K da dicotomia) − {m}", métrica=col,
                             **test(Hh[col] - Bm)))
    md += [pd.DataFrame(rows).to_markdown(index=False), "\n",
           H.groupby("ds")[["test_all", "test_new", "all", "new"]].mean().round(3).to_markdown(), "\n"]

# ------------------------------------- SimGCD com o K̂ da distância fixa (RQ3)
G = load("simgcd_keuclid.csv")
if G is not None and H is not None:
    md.append("## 5. SimGCD: K da dicotomia aprendida vs. K da distância fixa\n")
    Gg, Hh = G.set_index(K), H.set_index(K)
    rows = [dict(comparação="K aprendido − K distância fixa", métrica=c, **test(Hh[c] - Gg[c]))
            for c in ("test_all", "test_new", "all", "new")]
    md += [pd.DataFrame(rows).to_markdown(index=False), "\n",
           G.groupby("ds")[["test_all", "test_new", "k_est"]].mean().round(3).to_markdown(), "\n"]

(R / "revisao.md").write_text("\n".join(md))
print("\n".join(md))
