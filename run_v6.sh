#!/usr/bin/env bash
# Versão 6: protocolo final (PCA sem whitening, ajustado em L ∪ U), sementes 20-24.
# Uso: bash run_v6.sh [series|omniglot|all] [sementes] [classificadores]
#   bash run_v6.sh series      # séries: principal + escala (~1 h)
#   bash run_v6.sh omniglot    # Omniglot: principal (HOG, DINOv2) + escala DINOv2 (~3 h)
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
MODE=${1:-all}
SEEDS=${2:-5}
CLFS=${3:-logreg,hgb}
SEED0=20
OUT=results_v6
mkdir -p $OUT

SETS=()
if [ "$MODE" = series ] || [ "$MODE" = all ]; then
  for D in ShapesAll NonInvasiveFetalECGThorax1 Crop SwedishLeaf; do
    [ -f ts_$D.npz ] || "$PY" features_ts.py "$D" ts_$D.npz
    SETS+=(ts_$D)
  done
fi
if [ "$MODE" = omniglot ] || [ "$MODE" = all ]; then
  "$PY" get_omniglot.py
  [ -f omniglot_hog.npz ]    || "$PY" features.py data/omniglot omniglot_hog.npz
  [ -f omniglot_dinov2.npz ] || "$PY" features_cnn.py data/omniglot omniglot_dinov2.npz --model dinov2_vits14
  SETS+=(omniglot_dinov2 omniglot_hog)
fi

for F in "${SETS[@]}"; do
  echo "=== $F ==="
  ONLY=main,scale
  [ "$F" = omniglot_hog ] && ONLY=main
  "$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs "$CLFS" \
        --seed0 $SEED0 --only $ONLY --out $OUT/$F
  "$PY" summarize.py $OUT/$F > /dev/null
  "$PY" stats.py $OUT/$F > /dev/null
  "$PY" plot_scale.py $OUT/$F > /dev/null
done
[ -d $OUT/omniglot_hog ] && [ -d $OUT/omniglot_dinov2 ] && \
  "$PY" stats.py $OUT/omniglot_hog $OUT/omniglot_dinov2 > $OUT/testes_omniglot.md
echo "pronto: zip -r resultados_v6.zip $OUT *.log"
