"""Escolha do pré-processamento com SEMENTES DE DESENVOLVIMENTO (0-2), critério que só
olha para os baselines euclidianos (k-means e Ward com K oráculo).

    python choose_prep.py ts_SwedishLeaf,ts_Crop,omniglot_hog   (arquivos .npz na pasta)
Resultado obtido (média de 3 sementes, k-means com K oráculo):
                  whiten 64  sem whiten 64  whiten 32  whiten 16
    Crop             0,475       0,606        0,606      0,608
    SwedishLeaf      0,378       0,796        0,596      0,720
    ECG fetal        0,724       0,775        0,783      0,829
    Omniglot HOG     0,507       0,559        0,529      0,502
    média            0,521       0,684        0,628      0,665   -> sem whitening, 64
"""
import sys, numpy as np, pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import experiments as ex, dichotomy_owl as do

def split_idx(y, n_known, n_new, seed):
    rng = np.random.default_rng(seed)
    allc = np.unique(y)
    known = rng.choice(allc, n_known, replace=False)
    new = rng.choice(np.setdiff1d(allc, known), n_new, replace=False)
    L, U = [], []
    for c in known:
        idx = rng.permutation(np.flatnonzero(y == c)); L += list(idx[:10]); U += list(idx[10:17])
    for c in new:
        idx = rng.permutation(np.flatnonzero(y == c)); U += list(idx[:15])
    return np.array(L), np.array(U), new


CONF = {"whiten 64": (True, 64), "sem whiten 64": (False, 64), "whiten 32": (True, 32), "whiten 16": (True, 16)}

def omni_split(y, split, seed, novelty, n_known=100, n_new=20):
    rng = np.random.default_rng(seed)
    bg = np.unique(y[split == "images_background"]); ev = np.unique(y[split == "images_evaluation"])
    known = rng.choice(bg, n_known, replace=False)
    new = rng.choice(np.setdiff1d(bg, known) if novelty == "near" else ev, n_new, replace=False)
    L, U = [], []
    for c in known:
        idx = rng.permutation(np.flatnonzero(y == c)); L += list(idx[:10]); U += list(idx[10:17])
    for c in new:
        idx = rng.permutation(np.flatnonzero(y == c)); U += list(idx[:15])
    return np.array(L), np.array(U), new, n_new

rows = []
for name in sys.argv[1].split(","):
    path = f"{name}.npz"
    d = np.load(path); y = d["y"]
    for seed in (0, 1, 2):
        if "series" in d.files:
            n_cls = len(np.unique(y)); n_new = round(n_cls / 3)
            L, U, new = split_idx(y, n_cls - n_new, n_new, seed)
            F = ex.minirocket_features(d["series"], np.r_[L, U], seed)
        else:
            L, U, new, n_new = omni_split(y, d["split"], seed, "far")
            F = d["X"]
        fit = np.r_[L, U]
        Zs = StandardScaler().fit(F[fit]).transform(F)
        for cname, (wh, nc) in CONF.items():
            Z = PCA(min(nc, len(fit) // 4), whiten=wh, random_state=seed).fit(Zs[fit]).transform(Zs).astype(np.float32)
            Xu, yu = Z[U], y[U]; m = np.isin(yu, new); Xn, yn = Xu[m], yu[m]
            rows.append(dict(ds=name, seed=seed, config=cname,
                kmeans=do.cluster_acc(yn, KMeans(n_new, n_init=10, random_state=seed).fit_predict(Xn))[0],
                ward=do.cluster_acc(yn, AgglomerativeClustering(n_new, linkage="ward").fit_predict(Xn))[0]))
        print(name, seed, flush=True)
df = pd.DataFrame(rows); df.to_csv(f"diag2_{sys.argv[1].replace(',', '_')}.csv", index=False)
print(df.groupby(["ds", "config"])[["kmeans", "ward"]].mean().round(3).to_string())
