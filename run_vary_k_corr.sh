#!/usr/bin/env bash
# Bias correction of K̂ on the same runs as run_vary_k.sh (needs results_vary_k/*/vary_k.csv
# for the baselines). Results: results_vary_k/<set>/vary_k_corr.csv and
# results_vary_k/vary_k_corr.md. Can be stopped and restarted.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "using $PY ($($PY --version))"
SETS=${SETS:-"omniglot_dinov2 cub_dinov2 ts_ShapesAll omniglot_hog"}
for F in $SETS; do
  case $F in
    cub_dinov2)   KS=0,5,10,20,30 ;;
    ts_ShapesAll) KS=0,5,10,15,20 ;;
    *)            KS=0,5,10,20,40 ;;
  esac
  echo "=== $F  K in $KS ==="
  "$PY" vary_k_corr.py --features $F.npz --ks $KS 2>&1 | tee -a vary_k_corr_$F.log
done
"$PY" summarize_vary_k_corr.py
echo "done: zip -r vary_k_corr.zip results_vary_k/*/vary_k_corr.csv results_vary_k/vary_k_corr.md"
