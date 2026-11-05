"""Sensitivity to the number of novel classes K (question from a reader of the paper).

    python vary_k.py --features omniglot_dinov2.npz --ks 0,5,10,20,40

The known classes are fixed (100 in Omniglot and CUB, 40 in ShapesAll) and only the
number of novel classes K changes. In each seed the known classes are drawn first, so
for a given seed they are the same for every K, and so is the calibration scenario
(25 % of the known classes as pseudo-novel). If K̂ follows K, the method counts;
if K̂ stays near the calibration size, the calibration imposes a value.

Methods, all on the same split:
  dicotomia-hgb + ruído        the proposed method (prototype bank)
  dicotomia-euclid + ruído     the same pipeline with a calibrated fixed distance
  SS-kmeans (K estimado)       Vaze et al. K estimation + SS-k-means, with and without whitening
  SimGCD raso (K da dicotomia) shallow SimGCD head with K̂ of the proposed method
  SimGCD raso (K estimado)     shallow SimGCD head with the Vaze et al. estimate, with and without whitening
  SimGCD raso (K oráculo)      shallow SimGCD head with the true K (reference)

K = 0 (no novel class) measures false discovery. The Vaze et al. search starts at
n_known + 1, so SS-k-means and SimGCD (K estimado) report at least one novel class.

Rows are appended to results_vary_k/<features>/vary_k.csv after every run, and runs
already in the file are skipped, so the script can be stopped and restarted.
"""
import argparse
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

import dichotomy_owl as do
import experiments as E
import experiments_review as R


def acc(y, p, is_old):
    a, o, n = do.gcd_acc(y, p, is_old)
    return a, o, (n if (~is_old).any() else np.nan)


def ss_kmeans_row(D, n_known, seed):
    Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
    classes = np.unique(yl)
    k_tot = E.estimate_k(Xl, yl, Xu, seed)
    _, C, _ = E.ss_kmeans(Xl, yl, Xu, k_tot, seed)
    lt = E.sqdist(Xt, C).argmin(1)
    pt = np.where(lt < len(classes), classes[np.minimum(lt, len(classes) - 1)], 10_000 + lt)
    return k_tot, pt


def one_run(data, n_known, K, novelty, seed):
    rows = []
    base = dict(novelty=novelty, seed=seed, k_true=K)
    for whiten in (False, True):
        D = R.split(data, n_known, K, novelty, seed, whiten)
        Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
        is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])

        def add(method, k_est, pt, **kw):
            ta, to, tn = acc(yt, pt, is_old_t)
            rows.append(dict(base, method=method, whiten=whiten, k_est=int(k_est),
                             test_all=ta, test_old=to, test_new=tn, **kw))

        # baselines with the Vaze et al. estimate (with and without whitening)
        t0 = time.time()
        k_tot, pt = ss_kmeans_row(D, n_known, seed)
        add("SS-kmeans (K estimado)", k_tot - n_known, pt, secs=time.time() - t0)
        _, pt = R.simgcd_shallow(Xl, yl, Xu, Xt, k_tot, seed)
        add("SimGCD raso (K estimado)", k_tot - n_known, pt)
        if whiten:
            continue
        # the proposed method and the fixed-distance ablation (no whitening, as in the paper)
        k_hat = None
        for clf in ("hgb", "euclid"):
            t0 = time.time()
            calib = do.calibrate(Xl, yl, clf, seed)
            out = do.run_open_world(Xl, yl, Xu, clf, seed, calib, noise=True)
            pt = do.classify_with_bank(out["dic"], Xt, out["protos"], out["proto_y"])
            auroc = roc_auc_score(~is_new_u, out["score"]) if K > 0 else np.nan
            rej = out["rejected"]
            add(f"dicotomia-{clf} + ruído", out["n_new"], pt, auroc=auroc,
                rej_rate=rej.mean(), true_new_rate=is_new_u.mean(),
                cut=calib.cut, min_size=calib.min_size, secs=time.time() - t0)
            if clf == "hgb":
                k_hat = out["n_new"]
        _, pt = R.simgcd_shallow(Xl, yl, Xu, Xt, n_known + k_hat, seed)
        add("SimGCD raso (K da dicotomia)", k_hat, pt)
        _, pt = R.simgcd_shallow(Xl, yl, Xu, Xt, n_known + K, seed)
        add("SimGCD raso (K oráculo)", K, pt)
    return rows


def max_k(data, n_known):
    if "series" in data:
        return len(np.unique(data["y"])) - n_known
    if E.is_ssb(data):
        return min(len(np.unique(data["y"][data["split"] == s])) for s in ("hard", "easy"))
    return 10 ** 6


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True)
    ap.add_argument("--ks", required=True, help="e.g. 0,5,10,20,40")
    ap.add_argument("--n-known", type=int, default=None,
                    help="default: 100 in Omniglot and CUB, 2/3 of the classes in the series")
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--seed0", type=int, default=20)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    data, n_known, _ = R.setup(a.features, n_known_arg=a.n_known)
    ks = [int(k) for k in a.ks.split(",")]
    top = max_k(data, n_known)
    if any(k > top for k in ks):
        print(f"skipping K > {top}: not enough novel classes", flush=True)
        ks = [k for k in ks if k <= top]
    out = Path(a.out or Path("results_vary_k") / Path(a.features).stem)
    out.mkdir(parents=True, exist_ok=True)
    f = out / "vary_k.csv"
    done = set()
    if f.exists():
        old = pd.read_csv(f)
        done = set(zip(old.novelty, old.seed, old.k_true))
    print(f"{Path(a.features).stem}: {n_known} known, K in {ks}, {E.NOVELTIES}, "
          f"seeds {a.seed0}-{a.seed0 + a.seeds - 1}", flush=True)
    for K in ks:
        for novelty in E.NOVELTIES:
            for seed in range(a.seed0, a.seed0 + a.seeds):
                if (novelty, seed, K) in done:
                    continue
                t0 = time.time()
                rows = pd.DataFrame(one_run(data, n_known, K, novelty, seed))
                rows.to_csv(f, mode="a", header=not f.exists(), index=False)
                k = rows[rows.method == "dicotomia-hgb + ruído"].k_est.iloc[0]
                print(f"[K={K} {novelty} seed {seed}] K̂ = {k}  ({time.time() - t0:.0f} s)",
                      flush=True)
