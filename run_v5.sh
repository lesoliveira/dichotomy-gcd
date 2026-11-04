#!/usr/bin/env bash
# Execuções com PCA COM whitening (sementes 20-24), usadas no critério conservador: cada
# baseline recebe o melhor de com e sem whitening (final_tables.py). Resultados em results_v5/.
# Uso: bash run_v5.sh [sementes] [classificadores]
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
SEEDS=${1:-5}
CLFS=${2:-logreg,hgb}
SEED0=20
OUT=results_v5
mkdir -p $OUT

# garante as features
"$PY" get_omniglot.py
[ -f omniglot_hog.npz ]    || "$PY" features.py data/omniglot omniglot_hog.npz
[ -f omniglot_dinov2.npz ] || "$PY" features_cnn.py data/omniglot omniglot_dinov2.npz --model dinov2_vits14
for D in ShapesAll NonInvasiveFetalECGThorax1 Crop SwedishLeaf; do
  [ -f ts_$D.npz ] || "$PY" features_ts.py "$D" ts_$D.npz
done

# 1) experimento principal (com a variante híbrida) em todos os conjuntos
# 2) experimento de escala (só boosting) no Omniglot-DINOv2 e nas séries
for F in omniglot_dinov2 ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf omniglot_hog; do
  echo "=== $F ==="
  ONLY=main,scale
  [ "$F" = omniglot_hog ] && ONLY=main          # escala com HOG é opcional (lenta)
  "$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs "$CLFS" \
        --seed0 $SEED0 --only $ONLY --whiten --out $OUT/$F
  "$PY" summarize.py $OUT/$F > /dev/null
  "$PY" stats.py $OUT/$F > /dev/null
  "$PY" plot_scale.py $OUT/$F > /dev/null
done
"$PY" stats.py $OUT/omniglot_hog $OUT/omniglot_dinov2 > $OUT/testes_omniglot.md
echo "pronto: zip -r resultados_v5.zip $OUT *.log"
