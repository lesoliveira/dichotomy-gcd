"""Bias correction of K̂ (follow-up to vary_k.py).

    python vary_k_corr.py --features omniglot_dinov2.npz --ks 0,5,10,20,40

vary_k.py showed that K̂ = K + an almost constant offset, and that the offset is the
number of clusters formed by known samples rejected by mistake (the threshold always
rejects a fixed fraction 1 - TPR of the known classes). The offset is estimated here from
L alone, in the pseudo-novel scenario that the calibration already builds:

  spur_rate  = (clusters dominated by known samples in the pseudo scenario, after the
                noise rule with the calibrated m) / (known samples rejected there)
  n_rej_kn   = expected number of known samples of U rejected by mistake, without labels:
                accepted(U) * (1 - TPR) / TPR   (accepted samples are mostly known)
  K̂₀         = spur_rate * n_rej_kn                         ("rate" correction)
  K̂_corr     = max(0, K̂ - round(K̂₀))

"binom" correction: K̂₀ = sum over known classes c of P(Binomial(n_c, q_c) >= m), where q_c is
the out-of-fold rejection rate of the labelled samples of c and n_c = (U samples accepted as
c) / (1 - q_c); i.e. the expected number of known classes with at least m rejected samples.

Also recorded: "pseudo" correction = K̂_pseudo - n_pseudo without rescaling, and the true
number of known-dominated clusters in U (uses labels of U, for evaluation only).

Incorporation with the corrected count: the round(K̂₀) discovered clusters that look most
like known classes (highest mean max known-class score) go back to their argmax known
class, the rest stay as novel prototypes ("bank corr").

Methods per run: dichotomy (hgb) and the fixed distance (euclid), each raw and corrected,
and the shallow SimGCD head with the corrected K̂ of the dichotomy. Runs already in the
output file are skipped.
"""
import argparse
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import adjusted_rand_score, roc_auc_score

import dichotomy_owl as do
import experiments as E
import experiments_review as R
from vary_k import acc, max_k

warnings.filterwarnings("ignore", category=RuntimeWarning)


def calibrate_stats(Xl, yl, clf_name, seed, frac=0.25, n_proto=6):
    """do.calibrate, line by line (same random draws, same result), plus the counts
    needed for the correction."""
    rng = np.random.default_rng(seed + 1000)
    classes = np.unique(yl)
    pseudo = rng.choice(classes, max(2, int(frac * len(classes))), replace=False)
    kn = np.setdiff1d(classes, pseudo)
    m_kn, m_ps = np.isin(yl, kn), np.isin(yl, pseudo)
    proto_mask = np.zeros(len(yl), bool)
    for c in kn:
        idx = np.flatnonzero(yl == c)
        proto_mask[rng.permutation(idx)[:n_proto]] = True
    Xp, yp = Xl[proto_mask], yl[proto_mask]
    dic = do.Dichotomizer(clf_name, seed).fit(Xp, yp)
    test_known = m_kn & ~proto_mask
    Xq = np.vstack([Xl[test_known], Xl[m_ps]])
    yq = np.r_[yl[test_known], yl[m_ps]]
    is_new = np.r_[np.zeros(test_known.sum()), np.ones(m_ps.sum())].astype(bool)
    S = do.class_scores(dic, Xq, Xp, yp, kn).max(1)
    grid = np.quantile(S, np.linspace(0.01, 0.99, 99))
    J = [((S[~is_new] >= t).mean() + (S[is_new] < t).mean()) for t in grid]
    reject_thr = float(grid[int(np.argmax(J))])
    known_tpr = float((S[~is_new] >= reject_thr).mean())
    Xn, yn = Xl[m_ps], yl[m_ps]
    P = dic.proba_matrix(Xn, Xn)
    D = 1 - (P + P.T) / 2
    np.fill_diagonal(D, 0)
    best = (-1, 0.5)
    for cut in np.linspace(0.05, 0.95, 19):
        lab = AgglomerativeClustering(n_clusters=None, metric="precomputed", linkage="average",
                                      distance_threshold=1 - cut).fit_predict(D)
        best = max(best, (adjusted_rand_score(yn, lab), float(cut)))
    cut = best[1]
    Rr = do.detect_and_cluster(dic, Xq, Xp, yp, reject_thr, cut, new_base=yl.max() + 1)
    best_m = (-1, 0, 1)
    for m in do.MIN_SIZE_GRID:
        pred, _ = do.apply_noise_rule(Rr["pred"], Rr["rej"], Rr["new_lab"], Rr["S"], Rr["classes"], m)
        best_m = max(best_m, (do.gcd_acc(yq, pred, ~is_new)[0], -m, m))
    m = best_m[2]
    calib = do.Calib(reject_thr, known_tpr, cut, m)
    pred, rej = do.apply_noise_rule(Rr["pred"], Rr["rej"], Rr["new_lab"], Rr["S"], Rr["classes"], m)
    n_spur, _ = spurious(pred, rej, ~is_new)
    st = dict(ps_k_hat=len(np.unique(pred[rej])) if rej.any() else 0, ps_n_new=len(pseudo),
              ps_spur=n_spur, ps_rej_known=int((Rr["rej"] & ~is_new).sum()))
    return calib, st


def spurious(pred, rej, is_known):
    """Discovered clusters whose majority is known samples (needs labels)."""
    n, ids = 0, []
    for k in np.unique(pred[rej]):
        mem = rej & (pred == k)
        if is_known[mem].mean() > 0.5:
            n += 1
            ids.append(k)
    return n, ids


def pipeline(dic, Xl, yl, Xu, calib, oof):
    """do.run_open_world(noise=True), keeping the class scores."""
    thr = float(np.quantile(oof, 1.0 - calib.known_tpr))
    Rr = do.detect_and_cluster(dic, Xu, Xl, yl, thr, calib.cut, new_base=yl.max() + 1)
    pred, rej = do.apply_noise_rule(Rr["pred"], Rr["rej"], Rr["new_lab"], Rr["S"], Rr["classes"],
                                    calib.min_size)
    return pred, rej, Rr


def class_rates(Rr, oof, yl, thr):
    """Per known class: rejection rate of its labelled samples out of fold (q_c) and the
    number of U samples accepted as that class (no labels of U)."""
    classes = Rr["classes"]
    qc = np.array([(oof[yl == c] < thr).mean() for c in classes])
    acc_pred = Rr["pred"][~Rr["rej"]]
    nacc = np.array([(acc_pred == c).sum() for c in classes])
    return qc, nacc


def binom_offset(Rr, oof, yl, thr, m):
    """Expected number of known classes with at least m of their U samples rejected:
    sum_c P(Binomial(n_c, q_c) >= m), with n_c = accepted_c / (1 - q_c). Assumes that the
    rejected samples of one known class form one cluster and that classes do not mix."""
    from scipy.stats import binom
    qc, nacc = class_rates(Rr, oof, yl, thr)
    n = np.rint(nacc / np.clip(1 - qc, 0.05, 1)).astype(int)
    return float(binom.sf(m - 1, n, qc).sum())


def cluster_info(pred, rej, Rr, is_known):
    """size:known fraction:mean max known score, per discovered cluster (evaluation only)."""
    out = []
    for k in np.unique(pred[rej]):
        mem = rej & (pred == k)
        out.append(f"{mem.sum()}:{is_known[mem].mean():.2f}:{Rr['S'][mem].max(1).mean():.3f}")
    return " ".join(out)


def drop_known_like(pred, rej, Rr, n_drop):
    """Send the n_drop most known-like discovered clusters back to their argmax known class."""
    pred, rej = pred.copy(), rej.copy()
    ks = np.unique(pred[rej])
    if n_drop <= 0 or len(ks) == 0:
        return pred, rej
    S, classes = Rr["S"], Rr["classes"]
    like = np.array([S[rej & (pred == k)].max(1).mean() for k in ks])
    for k in ks[np.argsort(-like)[:n_drop]]:
        mem = np.flatnonzero(rej & (pred == k))
        pred[mem] = classes[S[mem].argmax(1)]
        rej[mem] = False
    return pred, rej


def one_run(data, n_known, K, novelty, seed):
    rows = []
    D = R.split(data, n_known, K, novelty, seed)
    Xl, yl, Xu, yu, Xt, yt = (D[k] for k in ("Xl", "yl", "Xu", "yu", "Xt", "yt"))
    is_new_u, is_old_t = np.isin(yu, D["new"]), np.isin(yt, D["known"])
    base = dict(novelty=novelty, seed=seed, k_true=K)
    for clf in ("hgb", "euclid"):
        t0 = time.time()
        calib, st = calibrate_stats(Xl, yl, clf, seed)
        dic = do.Dichotomizer(clf, seed).fit(Xl, yl)
        oof = do.oof_known_scores(Xl, yl, clf, seed)
        pred, rej, Rr = pipeline(dic, Xl, yl, Xu, calib, oof)
        k_raw = len(np.unique(pred[rej])) if rej.any() else 0
        thr = float(np.quantile(oof, 1.0 - calib.known_tpr))
        n_acc = int((Rr["score"] >= thr).sum())
        tpr = calib.known_tpr
        n_rej_kn = n_acc * (1 - tpr) / max(tpr, 1e-6)
        rate = st["ps_spur"] / max(st["ps_rej_known"], 1)
        k0 = {"rate": rate * n_rej_kn, "pseudo": st["ps_k_hat"] - st["ps_n_new"],
              "binom": binom_offset(Rr, oof, yl, thr, calib.min_size)}
        true_spur, _ = spurious(pred, rej, ~is_new_u)
        qc, nacc = class_rates(Rr, oof, yl, thr)
        auroc = roc_auc_score(~is_new_u, Rr["score"]) if K > 0 else np.nan
        common = dict(base, cut=calib.cut, min_size=calib.min_size, tpr=tpr, n_rej_kn_est=n_rej_kn,
                      n_rej_kn_true=int((Rr["rej"] & ~is_new_u).sum()), true_spur=true_spur,
                      spur_rate=rate, auroc=auroc, qc=" ".join(f"{v:.2f}" for v in qc),
                      nacc=" ".join(map(str, nacc)), clusters=cluster_info(pred, rej, Rr, ~is_new_u),
                      **st)
        for corr in ("none", "rate", "pseudo", "binom"):
            n_drop = 0 if corr == "none" else max(0, int(round(k0[corr])))
            p2, r2 = drop_known_like(pred, rej, Rr, n_drop)
            pt = do.classify_with_bank(dic, Xt, np.vstack([Xl, Xu[r2]]), np.r_[yl, p2[r2]])
            ta, to, tn = acc(yt, pt, is_old_t)
            k_corr = max(0, k_raw - n_drop)
            rows.append(dict(common, method=f"dicotomia-{clf}", corr=corr,
                             k0=k0.get(corr, 0.0), k_raw=k_raw, k_est=k_corr,
                             test_all=ta, test_old=to, test_new=tn, secs=time.time() - t0))
            if clf == "hgb" and corr != "none":
                _, pt = R.simgcd_shallow(Xl, yl, Xu, Xt, n_known + k_corr, seed)
                ta, to, tn = acc(yt, pt, is_old_t)
                rows.append(dict(base, method="SimGCD raso (K da dicotomia)", corr=corr,
                                 k_raw=k_raw, k_est=k_corr, test_all=ta, test_old=to, test_new=tn))
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--features", required=True)
    ap.add_argument("--ks", required=True)
    ap.add_argument("--n-known", type=int, default=None)
    ap.add_argument("--seeds", type=int, default=5)
    ap.add_argument("--seed0", type=int, default=20)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    data, n_known, _ = R.setup(a.features, n_known_arg=a.n_known)
    ks = [k for k in map(int, a.ks.split(",")) if k <= max_k(data, n_known)]
    out = Path(a.out or Path("results_vary_k") / Path(a.features).stem)
    out.mkdir(parents=True, exist_ok=True)
    f = out / "vary_k_corr.csv"
    done = set()
    if f.exists():
        old = pd.read_csv(f)
        done = set(zip(old.novelty, old.seed, old.k_true))
    print(f"{Path(a.features).stem}: {n_known} known, K in {ks}, {E.NOVELTIES}", flush=True)
    for K in ks:
        for novelty in E.NOVELTIES:
            for seed in range(a.seed0, a.seed0 + a.seeds):
                if (novelty, seed, K) in done:
                    continue
                t0 = time.time()
                rows = pd.DataFrame(one_run(data, n_known, K, novelty, seed))
                rows.to_csv(f, mode="a", header=not f.exists(), index=False)
                h = rows[(rows.method == "dicotomia-hgb")].set_index("corr")
                print(f"[K={K} {novelty} seed {seed}] K̂ raw {h.k_raw.iloc[0]}  "
                      f"rate {h.k_est['rate']}  pseudo {h.k_est['pseudo']}  binom {h.k_est['binom']}  "
                      f"(true spurious {h.true_spur.iloc[0]}, {time.time() - t0:.0f} s)", flush=True)
