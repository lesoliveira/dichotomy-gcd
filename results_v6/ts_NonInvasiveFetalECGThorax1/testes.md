# Wilcoxon pareado — ts_NonInvasiveFetalECGThorax1

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.105 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.083 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.127 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.148 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.136 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.152 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.054 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.02  | 3/5       | 0.75   |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.097 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.085 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.085 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.106 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.042 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.042 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.1   | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |      -1.4   | 2/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.004 | 2/5       | 0.75   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0     | 3/5       | 0.875  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.029 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |     -14.2   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.069 | 0/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.001 | 2/5       | 1      |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.126 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |       0.009 | 2/5       | 0.75   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.106 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.014 | 1/5       | 0.1875 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.092 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.025 | 0/5       | 0.0625 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |       0.075 | 4/5       | 0.1875 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |       0.02  | 4/5       | 0.4375 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.017 | 1/5       | 0.375  |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |       0.037 | 4/5       | 0.1875 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |       0.022 | 3/5       | 0.375  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |       0.038 | 4/5       | 0.3125 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.451 | 4/5       | 0.125  |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |      -0.016 | 2/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.091 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.069 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.113 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |       0.124 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.112 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |       0.129 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.051 | 4/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.017 | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.094 | 4/5       | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |       0.068 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.068 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |       0.09  | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |       0.011 | 3/5       | 0.8125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.011 | 3/5       | 0.8125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |       0.07  | 3/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -2.4   | 1/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0.004 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.017 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.033 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |     -13.4   | 0/5       | 0.0625 |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.031 | 1/5       | 0.3125 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |      -0.01  | 0/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.103 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |      -0.029 | 0/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.066 | 4/5       | 0.375  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.02  | 1/5       | 0.1875 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |       0.07  | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |      -0.012 | 2/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |       0.057 | 3/5       | 0.3125 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |       0.033 | 4/5       | 0.125  |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.046 | 0/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |       0.079 | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |       0.064 | 4/5       | 0.125  |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |       0.08  | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.493 | 5/5       | 0.0625 |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.05  | 1/5       | 0.125  |