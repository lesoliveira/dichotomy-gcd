"""Testes de Wilcoxon pareados (por semente e cenário) para as comparações do artigo.

    python stats.py results/omniglot_dinov2            -> results/omniglot_dinov2/testes.md
    python stats.py results/omniglot_hog results/omniglot_dinov2   (também HOG vs DINOv2)

Os pares são (cenário, semente). near e far compartilham as classes conhecidas da
mesma semente, então os pares não são totalmente independentes: reporte isso.
"""
import sys
from pathlib import Path

import pandas as pd
from scipy.stats import wilcoxon

SS = "SS-kmeans (K oráculo)"
SSP = "SS-kmeans + protótipos (K oráculo)"
SSE = "SS-kmeans (K estimado)"


def paired(df, a, b, col, keys=("novelty", "seed")):
    A = df[df.method == a].set_index(list(keys))[col]
    B = df[df.method == b].set_index(list(keys))[col]
    d = (A - B).dropna()
    if d.empty:
        return None
    p = wilcoxon(d).pvalue if (d != 0).any() else 1.0
    return dict(A=a, B=b, métrica=col, n=len(d), dif_média=round(d.mean(), 3),
                A_vence=f"{int((d > 0).sum())}/{len(d)}", p=round(p, 4))


def comparisons(R):
    g, s, d = (pd.read_csv(R / f) for f in ("gcd.csv", "descoberta.csv", "deteccao.csv"))
    clfs = sorted({m.split()[0] for m in g.method if m.startswith("dicotomia-")})
    rows = []
    for c in clfs:
        prop = f"{c} + ruído"
        for col in ("test_all", "test_old", "test_new", "all", "new"):
            rows += [paired(g, prop, SS, col), paired(g, prop, SSP, col), paired(g, prop, SSE, col)]
        # erro absoluto na estimativa do número de classes novas (menor é melhor)
        k_true = g[g.method == SS].set_index(["novelty", "seed"]).k_est
        ge = g.join(k_true.rename("k_true"), on=["novelty", "seed"])
        ge["k_err"] = (ge.k_est - ge.k_true).abs()
        rows += [paired(ge, prop, SSE, "k_err")]
        for col in ("test_all", "test_new", "all", "k_est"):
            rows += [paired(g, prop, c, col)]                       # efeito da regra de ruído
        rows += [paired(g, f"{c} + merge-back", c, "test_new")]
        hyb = f"{c} + híbrido"                                      # variante híbrida
        for col in ("test_all", "test_new", "all", "new"):
            rows += [paired(g, hyb, prop, col), paired(g, hyb, SSE, col)]
        rows += [paired(s, f"{c} K auto + Ward", "kmeans (K oráculo)", "acc"),
                 paired(s, f"{c} K auto + Ward", f"{c} (K auto)", "acc")]
        for b in ("kmeans (K oráculo)", "aglom. ward (K oráculo)", "NCA + kmeans (K oráculo)",
                  "kmeans (K silhueta)"):
            rows += [paired(s, f"{c} (K auto)", b, "acc")]
        rows += [paired(d, c, "LR-MSP", "auroc")]
    return pd.DataFrame([r for r in rows if r])


if __name__ == "__main__":
    dirs = [Path(a) for a in sys.argv[1:]]
    for R in dirs:
        t = comparisons(R)
        nota = "A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).\n\n"
        (R / "testes.md").write_text(f"# Wilcoxon pareado — {R.name}\n\n" + nota + t.to_markdown(index=False))
        print(f"## {R.name}\n", t.to_markdown(index=False), "\n")
    if len(dirs) == 2:
        a, b = (pd.read_csv(R / "gcd.csv") for R in dirs)
        rows = []
        for m in sorted(set(a.method) & set(b.method)):
            x = b[b.method == m].set_index(["novelty", "seed"]).test_all
            y = a[a.method == m].set_index(["novelty", "seed"]).test_all
            dd = (x - y).dropna()
            rows.append(dict(método=m, **{f"{dirs[1].name} − {dirs[0].name}": round(dd.mean(), 3)},
                             p=round(wilcoxon(dd).pvalue, 4) if (dd != 0).any() else 1.0))
        print("## representação (test_all)\n", pd.DataFrame(rows).to_markdown(index=False))
