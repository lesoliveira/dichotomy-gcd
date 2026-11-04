#!/usr/bin/env bash
# Ablação da dissimilaridade aprendida: o MESMO pipeline (calibração, limiar out-of-fold,
# corte, ruído, incorporação) com distância euclidiana fixa calibrada no lugar do
# dichotomizer. Rode depois de run_v6.sh. Resultados em results_v6_euclid/ (~20-30 min).
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
SEEDS=${1:-5}
OUT=results_v6_euclid
mkdir -p $OUT
for F in ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf omniglot_dinov2 omniglot_hog; do
  echo "=== $F ==="
  ONLY=main
  case $F in omniglot_dinov2|ts_ShapesAll) ONLY=main,scale;; esac
  "$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs euclid --scale-clf euclid \
        --seed0 20 --only $ONLY --out $OUT/$F
done
"$PY" compare_ablation.py results_v6 $OUT
echo "pronto: zip -r ablacao_euclid.zip $OUT ablacao*.log"
