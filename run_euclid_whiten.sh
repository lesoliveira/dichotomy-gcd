#!/usr/bin/env bash
# Completa a ablação: distância euclidiana fixa COM whitening (a versão sem whitening está em
# results_v6_euclid). Depois gera as tabelas finais com o critério conservador (cada método de
# comparação no seu melhor pré-processamento). ~20-30 min.
# Requer, na mesma pasta: results_v5, results_v6, results_v6_euclid e os .npz das features.
set -euo pipefail
cd "$(dirname "$0")"
PY=${PYTHON:-$(command -v python || command -v python3)}
echo "usando $PY ($($PY --version))"
for R in results_v5 results_v6 results_v6_euclid; do
  [ -d $R ] || { echo "falta a pasta $R (copie-a para esta pasta)"; exit 1; }
done
OUT=results_v6_euclid_w
mkdir -p $OUT
for F in ts_ShapesAll ts_NonInvasiveFetalECGThorax1 ts_Crop ts_SwedishLeaf omniglot_dinov2 omniglot_hog; do
  echo "=== $F ==="
  "$PY" experiments.py --features $F.npz --seeds 5 --seed0 20 --clfs euclid --only main \
        --whiten --out $OUT/$F
done
"$PY" final_tables.py --v6 results_v6 --v5 results_v5 --euc results_v6_euclid --eucw $OUT \
      --out results_final
echo "pronto: zip -r tabelas_finais.zip results_final $OUT"
