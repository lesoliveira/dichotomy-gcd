# Wilcoxon pareado — ts_ShapesAll

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.099 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.095 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.091 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.12  | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.117 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.108 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.074 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.068 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.07  | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.057 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.057 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.061 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |      -0.003 | 2/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.003 | 2/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.005 | 2/5       | 0.8125 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |       6.6   | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.006 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.002 | 2/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.03  | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |     -29.8   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.03  | 1/5       | 0.25   |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |       0.004 | 3/5       | 0.5625 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.095 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |       0.012 | 3/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.082 | 4/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.008 | 1/5       | 0.4375 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.053 | 4/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.014 | 2/5       | 0.5    |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |      -0.009 | 2/5       | 0.8125 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |      -0.075 | 1/5       | 0.375  |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.032 | 1/5       | 0.1875 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |      -0.043 | 3/5       | 0.8125 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |      -0.059 | 0/5       | 0.125  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.097 | 1/5       | 0.125  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.005 | 2/5       | 0.8125 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |      -0.007 | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.058 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.054 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.05  | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |       0.035 | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.032 | 3/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |       0.023 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.086 | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.08  | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.082 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |      -0.003 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |      -0.003 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |       0.001 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |      -0.033 | 3/5       | 0.8125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.033 | 3/5       | 0.8125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |      -0.025 | 3/5       | 0.8125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |       4.8   | 4/5       | 0.25   |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0.003 | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.002 | 3/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.028 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |     -35.6   | 0/5       | 0.0625 |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.014 | 1/5       | 0.75   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0.002 | 3/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.052 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |       0.006 | 3/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.088 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.003 | 1/5       | 0.625  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |      -0.001 | 2/5       | 0.875  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |      -0.001 | 2/5       | 0.75   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |      -0.025 | 3/5       | 0.8125 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |      -0.055 | 2/5       | 0.4375 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.024 | 1/5       | 0.625  |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |      -0.031 | 1/5       | 0.4375 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |      -0.048 | 1/5       | 0.25   |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.086 | 0/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.017 | 3/5       | 1      |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.11  | 0/5       | 0.0625 |