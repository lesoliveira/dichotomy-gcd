#!/usr/bin/env bash
# Experimentos pedidos na revisão, no protocolo final (sementes 20-24).
#   1. SimGCD raso nas mesmas features fixas        (todos os conjuntos, rápido)
#   2. agrupamento alternativo a partir de P(mesma)  (todos os conjuntos)
#   3. ablação de sensibilidade (12 configurações)   (só ABL_SETS, a parte lenta)
# Depois: review_tables.py -> results_review/revisao.md
#
# Uso: bash run_review.sh
#      ABL_SETS="omniglot_dinov2" bash run_review.sh     # ablação mais curta
#      SKIP_ABL=1 bash run_review.sh                      # só os itens 1 e 2
#
# Tempo estimado no Mac: itens 1 e 2 ~2 a 3 h no total (cada execução repete a
# calibração e o pipeline com hgb); item 3 ~1 h 30 por conjunto de Omniglot ou CUB
# e ~45 min por série, para as 12 configurações. O padrão (3 conjuntos) dá ~4 h.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
SETS=${SETS:-"omniglot_dinov2 omniglot_hog cub_dinov2 ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf"}
ABL_SETS=${ABL_SETS:-"omniglot_dinov2 cub_dinov2 ts_ShapesAll"}

for F in $SETS; do
  [ -f $F.npz ] || { echo "falta $F.npz"; exit 1; }
  echo "=== $F: SimGCD raso e agrupamento ==="
  "$PY" experiments_review.py --features $F.npz --only simgcd,cluster
done
if [ -z "${SKIP_ABL:-}" ]; then
  for F in $ABL_SETS; do
    echo "=== $F: ablação ==="
    "$PY" experiments_review.py --features $F.npz --only ablation
  done
fi
"$PY" review_tables.py > /dev/null
echo "pronto: zip -r resultados_revisao.zip results_review"
