"""Séries temporais da UCR para o protocolo de mundo aberto.

Baixa um conjunto da UCR (via aeon), junta treino e teste, mantém só classes com
pelo menos 20 séries (o protocolo usa 20 por classe) e guarda as séries BRUTAS,
z-normalizadas. As features MiniRocket são calculadas dentro de experiments.py,
por semente, com os kernels ajustados SOMENTE nas séries rotuladas (L) -- assim
nenhuma estatística de U ou T entra na representação.

Uso:
    python features_ts.py ShapesAll ts_ShapesAll.npz
    python features_ts.py --list            # conjuntos sugeridos
    python features_ts.py --synthetic ts_synth.npz   # dados sintéticos p/ testar o código

Conjuntos sugeridos (muitas classes, >= 20 séries por classe):
    ShapesAll                    60 classes, 20 por classe, comprimento 512 (contornos)
    NonInvasiveFetalECGThorax1   42 classes, ~90 por classe, comprimento 750 (ECG)
    Crop                         24 classes, 1000 por classe, comprimento 46 (satélite)
    SwedishLeaf                  15 classes, 75 por classe, comprimento 128 (contornos)
"""
import argparse
from pathlib import Path

import numpy as np

SUGGESTED = ["ShapesAll", "NonInvasiveFetalECGThorax1", "Crop", "SwedishLeaf"]
MIN_PER_CLASS = 20


def znorm(S):
    mu = S.mean(1, keepdims=True)
    sd = S.std(1, keepdims=True)
    return ((S - mu) / np.where(sd > 1e-8, sd, 1.0)).astype(np.float32)


def finalize(S, labels, max_per_class, seed=0):
    rng = np.random.default_rng(seed)
    labels = np.asarray(labels).astype(str)
    keep = []
    names = []
    for c in np.unique(labels):
        idx = np.flatnonzero(labels == c)
        if len(idx) < MIN_PER_CLASS:
            print(f"  classe {c}: {len(idx)} séries < {MIN_PER_CLASS}, descartada")
            continue
        keep.append(rng.permutation(idx)[:max_per_class])
        names.append(c)
    keep = np.concatenate(keep)
    y = np.searchsorted(np.array(names), labels[keep])
    return znorm(S[keep]), y, np.array(names)


def load_ucr(name, data_dir):
    from aeon.datasets import load_classification
    X, y = load_classification(name, extract_path=str(data_dir))   # treino + teste juntos
    X = np.asarray(X, dtype=np.float64)
    if X.ndim == 3:
        if X.shape[1] != 1:
            raise SystemExit(f"{name} é multivariado ({X.shape[1]} canais); use um univariado")
        X = X[:, 0, :]
    if np.isnan(X).any():
        raise SystemExit(f"{name} tem valores faltantes/comprimento variável; escolha outro")
    return X, y


def synthetic(n_classes=36, per_class=40, length=128, seed=0):
    """Classes = combinações de formas de onda; só para testar o pipeline."""
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 1, length)
    S, y = [], []
    for c in range(n_classes):
        f1, f2 = rng.uniform(1, 8, 2)
        ph, a2, pos = rng.uniform(0, 2 * np.pi), rng.uniform(0.2, 1), rng.uniform(0.2, 0.8)
        base = np.sin(2 * np.pi * f1 * t + ph) + a2 * np.sin(2 * np.pi * f2 * t)
        base += 2 * np.exp(-((t - pos) ** 2) / 0.002)
        for _ in range(per_class):
            shift = rng.integers(-6, 7)
            S.append(np.roll(base, shift) * rng.uniform(0.8, 1.2) + rng.normal(0, 0.35, length))
            y.append(f"c{c:02d}")
    return np.array(S), np.array(y)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("name", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--synthetic", metavar="OUT")
    ap.add_argument("--max-per-class", type=int, default=60)
    ap.add_argument("--data-dir", default=str(Path(__file__).parent / "data" / "ucr"))
    args = ap.parse_args()
    if args.list:
        print(__doc__.split("Conjuntos sugeridos")[1]); raise SystemExit
    if args.synthetic:
        S, lab = synthetic()
        out, name = args.synthetic, "synthetic"
    else:
        if not (args.name and args.out):
            ap.error("informe <nome UCR> <saida.npz>")
        S, lab = load_ucr(args.name, args.data_dir)
        out, name = args.out, args.name
    S, y, names = finalize(S, lab, args.max_per_class)
    np.savez_compressed(out, series=S, y=y, class_names=names,
                        split=np.full(len(y), "all"), dataset=name)
    print(f"{name}: {len(names)} classes, {len(y)} séries, comprimento {S.shape[1]} -> {out}")
