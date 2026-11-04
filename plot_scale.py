"""Figura e tabela do experimento de escala (escala.csv).

    python plot_scale.py results_v5/omniglot_dinov2 [outra_pasta ...]
Gera <pasta>/escala.png e <pasta>/escala_resumo.md (média ± desvio sobre sementes e cenários).
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#8a8a85", "axes.labelcolor": "#3a3a37",
                     "xtick.color": "#5a5a55", "ytick.color": "#5a5a55"})
# paleta categórica validada (ordem fixa); proposta = azul, híbrido = laranja
COL = {"ruído": ("#2a78d6", "o", "-"), "híbrido": ("#eb6834", "s", "-"),
       "Kest": ("#1baf7a", "^", "--"), "Korac": ("#8a8a85", "v", ":"),
       "Kauto": ("#2a78d6", "o", "-"), "KautoWard": ("#eb6834", "s", "-"), "kmK": ("#8a8a85", "v", ":")}


def series(ax, df, method, key, label, metric):
    g = df[df.method == method].groupby("n_known")[metric]
    m, s = g.mean(), g.std()
    c, mk, ls = COL[key]
    ax.plot(m.index, m.values, ls, marker=mk, ms=5, lw=2, color=c, label=label)
    ax.fill_between(m.index, m - s, m + s, color=c, alpha=.10, lw=0)


def main(R):
    df = pd.read_csv(R / "escala.csv")
    clf = next(m.split()[0] for m in df.method if m.startswith("dicotomia-"))
    gcd, desc, det = (df[df.kind == k] for k in ("gcd", "desc", "det"))
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.6))
    a, b, c = axs
    for m, k, lab in [(f"{clf} + ruído", "ruído", "dicotomia + ruído"),
                      (f"{clf} + híbrido", "híbrido", "dicotomia + híbrido (Ward)"),
                      ("SS-kmeans (K estimado)", "Kest", "SS-k-means, K estimado"),
                      ("SS-kmeans (K oráculo)", "Korac", "SS-k-means, K oráculo")]:
        series(a, gcd, m, k, lab, "test_new")
    a.set_ylabel("acurácia nas classes novas (teste)")
    a.set_title("(a) Classes novas após incorporação", loc="left", fontsize=10)
    for m, k, lab in [(f"{clf} (K auto)", "Kauto", "dicotomia (K auto)"),
                      (f"{clf} K auto + Ward", "KautoWard", "K da dicotomia + Ward"),
                      ("kmeans (K oráculo)", "kmK", "k-means, K oráculo")]:
        series(b, desc, m, k, lab, "acc")
    b.set_ylabel("acurácia de descoberta (detecção oráculo)")
    b.set_title("(b) Agrupamento das novas", loc="left", fontsize=10)
    for m, k, lab in [(f"{clf} + ruído", "ruído", "dicotomia + ruído"),
                      ("SS-kmeans (K estimado)", "Kest", "SS-k-means, K estimado")]:
        series(c, gcd, m, k, lab, "k_err")
    c.set_ylabel("|K estimado − K real|")
    c.set_title("(c) Erro na estimativa de K", loc="left", fontsize=10)
    for ax in axs:
        ax.set_xscale("log")
        ks = sorted(df.n_known.unique())
        ax.set_xticks(ks); ax.set_xticklabels(ks)
        ax.set_xlabel("classes conhecidas (escala log)")
        ax.grid(axis="y", color="#e6e5e0", lw=.8)
        ax.legend(frameon=False, fontsize=7.5)
    fig.suptitle(R.name, x=0.01, ha="left", fontsize=10, color="#1f1f1d")
    fig.tight_layout()
    fig.savefig(R / "escala.png", dpi=200)

    def tab(d, cols):
        g = d.groupby(["n_known", "method"])[cols]
        mu, sd = g.mean(), g.std()
        out = mu.copy().astype(object)
        for col in cols:
            out[col] = [f"{x:.3f} ± {y:.3f}" for x, y in zip(mu[col], sd[col])]
        return out.reset_index().to_markdown(index=False)
    txt = (f"# Escala — {R.name}\n\n## GCD ponta a ponta\n\n"
           + tab(gcd, ["all", "new", "test_all", "test_new", "k_est", "k_err"])
           + "\n\n## Descoberta (detecção oráculo)\n\n" + tab(desc, ["acc", "k_est"])
           + "\n\n## Detecção\n\n" + tab(det, ["auroc"]) + "\n")
    (R / "escala_resumo.md").write_text(txt)
    print(txt)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        if (Path(a) / "escala.csv").exists():
            main(Path(a))
