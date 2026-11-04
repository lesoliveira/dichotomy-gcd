"""Tabelas finais com critério CONSERVADOR: cada método de comparação recebe, em cada
conjunto e para cada métrica, o melhor de dois pré-processamentos (PCA com e sem whitening).
O método proposto (dicotomia-hgb + ruído) é praticamente invariante ao whitening e usa a v6.

    python final_tables.py --v6 results_v6 --v5 results_v5 \
        --euc results_v6_euclid --eucw results_v6_euclid_w --out results_final

Pastas: v6 = sem whitening; v5 = com whitening (mesmas sementes 20-24 e partições);
euc/eucw = ablação com distância euclidiana fixa, sem/com whitening (eucw é opcional).
A escolha do melhor pré-processamento é feita com os próprios resultados de avaliação, o que
favorece os métodos de comparação (conservador contra o método proposto).
"""
import argparse
from pathlib import Path

import pandas as pd
from scipy.stats import wilcoxon

TS = ["ts_ShapesAll", "ts_NonInvasiveFetalECGThorax1", "ts_Crop", "ts_SwedishLeaf"]
OM = ["omniglot_dinov2", "omniglot_hog"]
CUB = ["cub_dinov2"]
ALL = OM + CUB + TS
K = ["ds", "novelty", "seed"]
OURS = {"gcd": "dicotomia-hgb + ruído", "descoberta": "dicotomia-hgb (K auto)",
        "deteccao": "dicotomia-hgb"}
COMP = {  # (arquivo, método, pasta sem whitening, pasta com whitening)
    "gcd": [("SS-kmeans (K estimado)", "v6", "v5"), ("SS-kmeans (K oráculo)", "v6", "v5"),
            ("SS-kmeans + protótipos (K oráculo)", "v6", "v5"),
            ("dicotomia-euclid + ruído", "euc", "eucw")],
    "descoberta": [("kmeans (K oráculo)", "v6", "v5"), ("aglom. ward (K oráculo)", "v6", "v5"),
                   ("NCA + kmeans (K oráculo)", "v6", "v5"), ("kmeans (K silhueta)", "v6", "v5"),
                   ("dicotomia-euclid (K auto)", "euc", "eucw")],
    "deteccao": [("LR-MSP", "v6", "v5"), ("1NN-dist", "v6", "v5"),
                 ("centroid-dist", "v6", "v5"), ("dicotomia-euclid", "euc", "eucw")],
}
METRICS = {"gcd": ["test_all", "test_new", "all", "new", "k_err"],
           "descoberta": ["acc"], "deteccao": ["auroc"]}
LOWER_BETTER = {"k_err"}


def load(root, kind):
    if root is None or not Path(root).exists():
        return None
    out = []
    for d in ALL:
        f = Path(root) / d / f"{kind}.csv"
        if f.exists():
            x = pd.read_csv(f); x["ds"] = d; out.append(x)
    if not out:
        return None
    df = pd.concat(out)
    if kind == "gcd":       # erro absoluto em K (K real vem da linha com K oráculo)
        kt = df[df.method == "SS-kmeans (K oráculo)"].set_index(K).k_est.rename("k_true")
        if len(kt):
            df = df.join(kt, on=K); df["k_err"] = (df.k_est - df.k_true).abs()
    return df


def best_of(frames, method, col, ds):
    """Escolhe, no conjunto ds, a versão (sem/com whitening) com melhor média em col."""
    cands = []
    for tag, df in frames:
        if df is None or col not in df:
            continue
        x = df[(df.method == method) & (df.ds == ds)]
        if len(x):
            cands.append((tag, x))
    if not cands:
        return None, None
    key = (lambda c: -c[1][col].mean()) if col in LOWER_BETTER else (lambda c: c[1][col].mean())
    tag, x = max(cands, key=key)
    return tag, x


def main(a):
    roots = dict(v6=a.v6, v5=a.v5, euc=a.euc, eucw=a.eucw)
    out_dir = Path(a.out); out_dir.mkdir(parents=True, exist_ok=True)
    md, tests, per_ds = ["# Tabelas finais (critério conservador)\n"], [], []
    for kind, comps in COMP.items():
        data = {t: load(r, kind) for t, r in roots.items()}
        ours = data["v6"][data["v6"].method == OURS[kind]]
        for col in METRICS[kind]:
            if col not in ours:
                continue
            row_ours = dict(tabela=kind, métrica=col, método=OURS[kind] + " (proposto)")
            for d in ALL:
                row_ours[d] = ours[ours.ds == d][col].mean()
            per_ds.append(row_ours)
            for method, nw, w in comps:
                if col == "k_err" and "oráculo" in method:
                    continue                      # K oráculo tem erro zero por definição
                frames = [("sem whiten", data[nw]), ("whiten", data[w])]
                picked, row = [], dict(tabela=kind, métrica=col, método=method)
                for d in ALL:
                    tag, x = best_of(frames, method, col, d)
                    if x is None:
                        continue
                    picked.append(x); row[d] = x[col].mean(); row[f"{d}_prep"] = tag
                per_ds.append(row)
                if not picked:
                    continue
                B = pd.concat(picked).set_index(K)[col]
                A = ours.set_index(K)[col]
                for grp, dss in (("todos", ALL), ("sem CUB", OM + TS), ("imagens", OM + CUB),
                                 ("séries", TS), ("Omniglot", OM), ("CUB", CUB)):
                    dd = (A - B).dropna()
                    dd = dd[dd.index.get_level_values(0).isin(dss)]
                    if dd.empty:
                        continue
                    wins = (dd < 0).sum() if col in LOWER_BETTER else (dd > 0).sum()
                    p = wilcoxon(dd).pvalue if (dd != 0).any() else 1.0
                    tests.append(dict(tabela=kind, métrica=col, comparação=f"proposto − {method}",
                                      grupo=grp, n=len(dd), dif=round(dd.mean(), 3),
                                      proposto_melhor=f"{int(wins)}/{len(dd)}", p=round(p, 4)))
    T = pd.DataFrame(tests); P = pd.DataFrame(per_ds)
    T.to_csv(out_dir / "testes_finais.csv", index=False); P.to_csv(out_dir / "por_conjunto.csv", index=False)
    md += ["## Wilcoxon pareado: proposto vs. cada comparação no seu melhor pré-processamento\n",
           "Para k_err, menor é melhor; `proposto_melhor` já conta os pares a favor do proposto.\n",
           T.to_markdown(index=False), "\n## Médias por conjunto\n",
           P[["tabela", "métrica", "método"] + [d for d in ALL if d in P]].round(3)
           .to_markdown(index=False),
           "\n## Pré-processamento escolhido para cada comparação\n",
           P[["tabela", "métrica", "método"] + [c for c in P if c.endswith("_prep")]]
           .dropna(how="all", subset=[c for c in P if c.endswith("_prep")]).to_markdown(index=False)]
    (out_dir / "tabelas.md").write_text("\n".join(md))
    print("\n".join(md[:4]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--v6", default="results_v6")
    ap.add_argument("--v5", default="results_v5")
    ap.add_argument("--euc", default="results_v6_euclid")
    ap.add_argument("--eucw", default="results_v6_euclid_w")
    ap.add_argument("--out", default="results_final")
    main(ap.parse_args())
