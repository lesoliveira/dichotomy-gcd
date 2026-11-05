#!/usr/bin/env bash
# Sensitivity to the number of novel classes K, known classes fixed (seeds 20-24).
# Needs the feature files of run_v6.sh / run_cub.sh (omniglot_*.npz, cub_dinov2.npz,
# ts_ShapesAll.npz). Results: results_vary_k/<set>/vary_k.csv, then the summary
# results_vary_k/vary_k.md and figures/vary_k.pdf.
# Can be stopped and restarted: finished runs are skipped.
#   bash run_vary_k.sh                 # all four settings
#   SETS="omniglot_dinov2" bash run_vary_k.sh
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "using $PY ($($PY --version))"
SETS=${SETS:-"omniglot_dinov2 cub_dinov2 ts_ShapesAll omniglot_hog"}
for F in $SETS; do
  case $F in
    cub_dinov2)   KS=0,5,10,20,30 ;;     # SSB Easy has only 32 classes
    ts_ShapesAll) KS=0,5,10,15,20 ;;     # 60 classes, 40 known
    *)            KS=0,5,10,20,40 ;;
  esac
  echo "=== $F  K in $KS ==="
  "$PY" vary_k.py --features $F.npz --ks $KS 2>&1 | tee -a vary_k_$F.log
done
"$PY" summarize_vary_k.py
echo "done: zip -r vary_k.zip results_vary_k figures/vary_k.pdf"
