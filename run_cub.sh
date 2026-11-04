#!/usr/bin/env bash
# CUB-200-2011 com DINOv2 congelado: o mesmo protocolo final do artigo (sementes 20-24).
#   1. extrai as features (baixa o CUB se faltar)
#   2. método + baselines sem whitening        -> results_v6/cub_dinov2
#   3. transferência (RQ1) com hgb              -> results_v6/cub_dinov2/transferencia_hgb.csv
#   4. baselines com whitening (critério conservador) -> results_v5/cub_dinov2
#   5. ablação com distância euclidiana fixa, sem e com whitening
#   6. tabelas finais com o CUB incluído        -> results_final
# Uso: bash run_cub.sh [sementes] [classificadores]
# Tempo estimado no Mac: extração ~5 min; experimentos ~1,5 a 2 h no total.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
SEEDS=${1:-5}
CLFS=${2:-logreg,hgb}
F=cub_dinov2

[ -f $F.npz ] || "$PY" features_cub.py data $F.npz --model dinov2_vits14

echo "=== $F: método e baselines (sem whitening) ==="
"$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs "$CLFS" --seed0 20 \
      --only main --out results_v6/$F
echo "=== $F: transferência (RQ1) ==="
"$PY" experiments.py --features $F.npz --seeds "$SEEDS" --seed0 20 --only transfer \
      --transfer-clf hgb --out results_v6/$F
echo "=== $F: baselines com whitening ==="
"$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs hgb --seed0 20 \
      --only main --whiten --out results_v5/$F
echo "=== $F: ablação com distância fixa ==="
"$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs euclid --seed0 20 \
      --only main --out results_v6_euclid/$F
"$PY" experiments.py --features $F.npz --seeds "$SEEDS" --clfs euclid --seed0 20 \
      --only main --whiten --out results_v6_euclid_w/$F

"$PY" summarize.py results_v6/$F > /dev/null
"$PY" stats.py results_v6/$F > /dev/null
"$PY" final_tables.py --v6 results_v6 --v5 results_v5 --euc results_v6_euclid \
      --eucw results_v6_euclid_w --out results_final
echo "pronto: zip -r resultados_cub.zip results_v6/$F results_v5/$F results_v6_euclid/$F results_v6_euclid_w/$F results_final"
