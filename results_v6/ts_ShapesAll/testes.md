# Wilcoxon pareado — ts_ShapesAll

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.128 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.105 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.152 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.183 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.142 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.205 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.062 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.062 | 4/5       | 0.1875 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.088 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.094 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.094 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.119 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.001 | 1/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.001 | 1/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.021 | 2/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |       0.8   | 2/5       | 0.9375 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.006 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.002 | 2/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.03  | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |     -29.8   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.03  | 1/5       | 0.25   |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.005 | 1/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.147 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.006 | 2/5       | 0.75   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.082 | 3/5       | 0.3125 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.008 | 1/5       | 0.3125 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.111 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.017 | 1/5       | 0.1875 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |       0.004 | 1/5       | 0.625  |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |      -0.049 | 2/5       | 0.625  |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.043 | 2/5       | 0.3125 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |      -0.006 | 3/5       | 0.875  |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |      -0.056 | 1/5       | 0.125  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.082 | 1/5       | 0.125  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.118 | 3/5       | 0.625  |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |      -0.005 | 2/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.087 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.065 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.111 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |       0.098 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.057 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |       0.12  | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.074 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.074 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.1   | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |       0.035 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.035 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |       0.06  | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |      -0.028 | 2/5       | 0.5625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.028 | 2/5       | 0.5625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |      -0.008 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -1     | 2/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0.003 | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.002 | 3/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.028 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |     -35.6   | 0/5       | 0.0625 |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.014 | 1/5       | 0.75   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0.001 | 2/5       | 0.75   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.112 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |       0.008 | 2/5       | 0.875  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.108 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.004 | 1/5       | 0.625  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |       0.056 | 3/5       | 0.625  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |      -0.005 | 1/5       | 0.625  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |      -0.013 | 2/5       | 1      |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |      -0.045 | 2/5       | 0.3125 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.051 | 1/5       | 0.1875 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |       0.005 | 1/5       | 0.625  |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |      -0.045 | 1/5       | 0.3125 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.071 | 0/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.129 | 3/5       | 0.625  |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.108 | 0/5       | 0.0625 |