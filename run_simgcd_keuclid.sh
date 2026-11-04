#!/usr/bin/env bash
# SimGCD raso com o K estimado pelo pipeline de distância fixa (results_v6_euclid).
# Compara com run_simgcd_khat.sh (K da dicotomia aprendida). ~20 a 30 min no Mac.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
for F in omniglot_dinov2 omniglot_hog cub_dinov2 ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf; do
  echo "=== $F ==="
  "$PY" experiments_review.py --features $F.npz --only simgcd_keuclid
done
"$PY" review_tables.py > /dev/null
echo "pronto: zip -r resultados_keuclid.zip results_review"
