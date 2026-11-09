"""Baselines without the 64-component PCA (question: is the PCA a handicap for them?).

    python baselines_fullfeat.py --features omniglot_dinov2.npz            # no PCA
    python baselines_fullfeat.py --features omniglot_dinov2.npz --pca 128  # 128 components

The dichotomy is NOT rerun: it keeps its 64-component PCA, and its estimate K̂ is read
from results_review/<set>/simgcd_khat.csv (the K̂ of the paper). Everything else runs on
the new representation (standardised features, or a PCA with --pca components, fitted
on L ∪ U as in the paper):

  K search of Vaze et al.            K estimated by k-means + labelled accuracy
  SS-kmeans (K estimado / oráculo)   semi-supervised k-means
  SimGCD raso (K estimado / oráculo / K da dicotomia)

Same seeds, scenarios and splits as the paper. Rows go to
results_fullfeat/<set>/<prep>.csv; finished runs are skipped.
"""
import argparse
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

import dichotomy_owl as do
import experiments as E
import experiments_review as R

warnings.filterwarnings("ignore", category=RuntimeWarning)


def standardise_only(Xfit, seed, n_comp=None):
    sc = StandardScaler().fit(Xfit)
    return lambda A: sc.transform(A).astype(np.float32)


def predict_ss(Xl, yl, Xu, Xt, k_tot, seed):
    classes = np.unique(yl)
    _, C, _ = E.ss_kmeans(Xl, yl, Xu, k_tot, seed)
    lt = E.sqdist(Xt, C).argmin(1)
    return np.where(lt < len(classes), classes[np.minimum(lt, len(classes) - 1)], 10_000 + lt)


def one_run(data, n_known, n_new, novelty, seed, k_hat):
    D = E.make_split(data, n_known, n_new, novelty, seed)
    Xl, yl, Xu, Xt, yt = D["Xl"], D["yl"], D["Xu"], D["Xt"], D["yt"]
    is_old = np.isin(yt, D["known"])
    base = dict(novelty=novelty, seed=seed, k_true=n_new, dim=Xl.shape[1])
    rows = []

    def add(method, k_est, pt, t0):
        a, o, n = do.gcd_acc(yt, pt, is_old)
        rows.append(dict(base, method=method, k_est=int(k_est), test_all=a, test_old=o,
                         test_new=n, secs=time.time() - t0))

    t0 = time.time()
    k_tot = E.estimate_k(Xl, yl, Xu, seed)
    add("SS-kmeans (K estimado)", k_tot - n_known, predict_ss(Xl, yl, Xu, Xt, k_tot, seed), t0)
    t0 = time.time()
    add("SS-kmeans (K oráculo)", n_new, predict_ss(Xl, yl, Xu, Xt, n_known + n_new, seed), t0)
    for name, k in (("SimGCD raso (K estimado)", k_tot - n_known),
                    ("SimGCD raso (K oráculo)", n_new),
                    ("SimGCD raso (K da dicotomia)", k_hat)):
        t0 = time.time()
        _, pt = R.simgcd_shallow(Xl, yl, Xu, Xt, n_known + k, seed)
        add(name, k, pt, t0)
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True)
    ap.add_argument("--pca", type=int, default=0, help="0 = no PCA (standardised features)")
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--seed0", type=int, default=20)
    a = ap.parse_args()
    data, n_known, n_new = R.setup(a.features)
    if a.pca == 0:
        E.make_prep = standardise_only
        prep = "full"
    else:
        E.N_PCA = a.pca
        prep = f"pca{a.pca}"
    stem = Path(a.features).stem
    kh = pd.read_csv(Path("results_review") / stem / "simgcd_khat.csv").set_index(["novelty", "seed"]).k_est
    out = Path("results_fullfeat") / stem
    out.mkdir(parents=True, exist_ok=True)
    f = out / f"{prep}.csv"
    done = set(zip(*pd.read_csv(f)[["novelty", "seed"]].values.T)) if f.exists() else set()
    print(f"{stem}: {prep}, {n_known} known, K = {n_new}, {E.NOVELTIES}", flush=True)
    for novelty in E.NOVELTIES:
        for seed in range(a.seed0, a.seed0 + a.seeds):
            if (novelty, seed) in done:
                continue
            t0 = time.time()
            rows = pd.DataFrame(one_run(data, n_known, n_new, novelty, seed, int(kh[(novelty, seed)])))
            rows.to_csv(f, mode="a", header=not f.exists(), index=False)
            r = rows.set_index("method")
            print(f"[{novelty} seed {seed}] dim {r.dim.iloc[0]}  K search {r.k_est['SS-kmeans (K estimado)']}"
                  f"  SimGCD: est {100 * r.test_all['SimGCD raso (K estimado)']:.1f}"
                  f"  K̂ {100 * r.test_all['SimGCD raso (K da dicotomia)']:.1f}"
                  f"  true {100 * r.test_all['SimGCD raso (K oráculo)']:.1f}  ({time.time() - t0:.0f} s)",
                  flush=True)
