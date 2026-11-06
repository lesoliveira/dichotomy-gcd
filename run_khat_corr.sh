#!/usr/bin/env bash
# Main SimGCD result with the bias-corrected K̂ (default K of every setting).
# Omniglot, CUB and ShapesAll come from run_vary_k_corr.sh (K = 20); this script runs
# the other three series at their default K, then writes results_vary_k/khat_corr.md.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "using $PY ($($PY --version))"
for FK in ts_NonInvasiveFetalECGThorax1:14 ts_Crop:8 ts_SwedishLeaf:5; do
  F=${FK%%:*}; K=${FK##*:}
  echo "=== $F  K = $K ==="
  "$PY" vary_k_corr.py --features $F.npz --ks $K 2>&1 | tee -a vary_k_corr_$F.log
done
"$PY" khat_corr_tables.py
echo "done: zip -r khat_corr.zip results_vary_k/*/vary_k_corr.csv results_vary_k/khat_corr.md"
