#!/usr/bin/env bash
# SimGCD raso com o número de classes estimado pela dicotomia (lido de results_v6).
# Rápido: ~20 a 30 min no Mac (o MiniRocket das séries é a parte mais lenta).
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
for F in omniglot_dinov2 omniglot_hog cub_dinov2 ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf; do
  echo "=== $F ==="
  "$PY" experiments_review.py --features $F.npz --only simgcd_khat
done
"$PY" review_tables.py > /dev/null
echo "pronto: zip -r resultados_khat.zip results_review"
