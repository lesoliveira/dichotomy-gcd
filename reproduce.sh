#!/usr/bin/env bash
# Reproduces every experiment of the paper, in order (evaluation seeds 20-24).
# Total time on a laptop CPU (Apple M-series): roughly one to two days, dominated by
# gradient boosting. Each stage can also be run on its own; see README.md.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
SETS6="omniglot_dinov2 omniglot_hog ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf"

# 1. features (Omniglot HOG and DINOv2, UCR series) + main experiment and scale, no whitening
bash run_v6.sh all
# 2. transfer of the learned similarity (RQ1)
for F in $SETS6; do
  "$PY" experiments.py --features $F.npz --seeds 5 --seed0 20 --only transfer \
        --transfer-clf hgb --out results_v6/$F
done
# 3. the same runs with PCA whitening (baselines receive the better of the two)
bash run_v5.sh
# 4. fixed-distance ablation, without and with whitening, then the final tables
bash run_ablation_euclid.sh
bash run_euclid_whiten.sh
# 5. CUB-200-2011 (downloads the dataset, extracts DINOv2 features, runs 1-4 for CUB)
bash run_cub.sh
# 6. SimGCD head, clustering alternatives and sensitivity analysis
bash run_review.sh
# 7. SimGCD with the K estimated by the learned dichotomy and by the fixed distance
bash run_simgcd_khat.sh
bash run_simgcd_keuclid.sh
# 8. sensitivity to the number of novel classes, bias correction of K̂, baselines without PCA
bash run_vary_k.sh
bash run_vary_k_corr.sh
bash run_fullfeat.sh
# 9. figures
"$PY" make_figures.py
"$PY" make_dataset_figure.py
"$PY" fig_dendrogram.py
echo "done: tables in results_final/tabelas.md, results_review/revisao.md, results_vary_k/*.md, results_fullfeat/fullfeat.md; figures in figures/"
