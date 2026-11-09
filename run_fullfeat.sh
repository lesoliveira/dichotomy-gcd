#!/usr/bin/env bash
# Baselines on the full standardised features (no PCA); the dichotomy keeps its K̂ from
# results_review. Results: results_fullfeat/<set>/full.csv, summary results_fullfeat/fullfeat.md.
# Can be stopped and restarted.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "using $PY ($($PY --version))"
for F in ${SETS:-ts_SwedishLeaf ts_Crop ts_NonInvasiveFetalECGThorax1 ts_ShapesAll cub_dinov2 omniglot_dinov2 omniglot_hog}; do
  "$PY" baselines_fullfeat.py --features $F.npz 2>&1 | tee -a fullfeat_$F.log
done
"$PY" summarize_fullfeat.py
echo "done: zip -r fullfeat.zip results_fullfeat"
