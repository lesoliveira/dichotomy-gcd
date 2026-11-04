"""Gera tabelas (média ± desvio) e a figura da RQ1 a partir de <pasta>/*.csv.

    python summarize.py results/omniglot_hog
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "results"


def ms(df, keys, cols):
    g = df.groupby(keys)[cols]
    m, s = g.mean(), g.std()
    out = m.copy().astype(object)
    for c in cols:
        out[c] = [f"{a:.3f} ± {b:.3f}" for a, b in zip(m[c], s[c])]
    return out.reset_index()


lines = []
for name, cols in [("deteccao", ["auroc"]),
                   ("descoberta", ["acc", "ari", "k_est"]),
                   ("gcd", ["all", "old", "new", "k_est", "test_all", "test_old", "test_new"]),
                   ("calibracao", ["rej_rate", "true_new_rate", "rej_recall_new",
                                   "known_tpr_target", "known_tpr_obs", "min_size"])]:
    src = "gcd" if name == "calibracao" else name
    if not (R / f"{src}.csv").exists():
        continue
    df = pd.read_csv(R / f"{src}.csv")
    if name == "calibracao":
        df = df[df.method.str.startswith("dicotomia")]
    t = ms(df, ["novelty", "method"], cols)
    lines += [f"## {name}", "", t.to_markdown(index=False), ""]

if (R / "ablacao.csv").exists():
    ab = pd.read_csv(R / "ablacao.csv")
    t = ms(ab, ["factor", "value"], ["auroc", "disc_acc", "disc_k", "k_est", "test_all", "test_new"])
    lines += ["## ablacao (logreg + ruído; média dos cenários)", "", t.to_markdown(index=False), ""]

if not (R / "transferencia.csv").exists():
    (R / "resumo.md").write_text("\n".join(lines)); print("\n".join(lines)); sys.exit()
tr = pd.read_csv(R / "transferencia.csv")
lines += ["## transferencia (AUC par-a-par em pares novo-novo)", "",
          ms(tr, ["novelty", "n_known"], ["pair_auc_new"]).to_markdown(index=False), ""]
(R / "resumo.md").write_text("\n".join(lines))

fig, ax = plt.subplots(figsize=(5.2, 3.4))
LAB = {"near": ("novas: mesmos alfabetos", "-"), "far": ("novas: alfabetos inéditos", "--"),
       "random": ("classes novas", "-")}
for nov in tr.novelty.unique():
    lab, ls = LAB.get(nov, (nov, "-"))
    g = tr[tr.novelty == nov].groupby("n_known").pair_auc_new
    m, s = g.mean(), g.std()
    ax.plot(m.index, m.values, ls, marker="o", color="#1f3b73", label=lab)
    ax.fill_between(m.index, m - s, m + s, color="#1f3b73", alpha=0.12)
ax.set_xscale("log")
ax.set_xlabel("número de classes conhecidas no treino do dichotomizer")
ax.set_ylabel("AUC par-a-par (classes novas)")
ax.grid(alpha=0.3)
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig(R / "rq1_transferencia.png", dpi=200)
print((R / "resumo.md").read_text())
