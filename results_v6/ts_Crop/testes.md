# Wilcoxon pareado — ts_Crop

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.039 | 4/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.055 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.073 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.117 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.125 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.125 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |      -0.055 | 0/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |      -0.03  | 0/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.01  | 3/5       | 0.75   |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |      -0.021 | 2/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |      -0.021 | 2/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.002 | 3/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |      -0.093 | 0/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.093 | 0/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |      -0.11  | 0/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |       0.2   | 2/5       | 0.9375 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |      -0     | 1/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.005 | 1/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.004 | 3/5       | 0.375  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |      -6.2   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |       0     | 1/5       | 1      |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.005 | 0/5       | 0.5    |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.068 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.015 | 1/5       | 0.5    |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |      -0.005 | 2/5       | 1      |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.002 | 2/5       | 0.875  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |      -0     | 2/5       | 1      |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.017 | 1/5       | 0.1875 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |      -0.127 | 0/5       | 0.0625 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |      -0.09  | 1/5       | 0.125  |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.035 | 2/5       | 0.3125 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |      -0.055 | 1/5       | 0.1875 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |      -0.042 | 0/5       | 0.0625 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.033 | 2/5       | 0.3125 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.015 | 2/5       | 0.8125 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |       0.025 | 4/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |      -0.018 | 3/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |      -0.002 | 1/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.016 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |      -0.021 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |      -0.012 | 1/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |      -0.012 | 2/5       | 0.6875 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |      -0.015 | 1/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.01  | 2/5       | 0.75   |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.05  | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |      -0.049 | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |      -0.049 | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |      -0.027 | 0/5       | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |      -0.1   | 1/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.1   | 1/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |      -0.117 | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -3     | 0/5       | 0.125  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |      -0.005 | 0/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |      -0.005 | 0/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.003 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |      -5     | 0/5       | 0.125  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.08  | 0/5       | 0.125  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0.014 | 3/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.03  | 4/5       | 0.3125 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |      -0.01  | 0/5       | 0.5    |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.04  | 3/5       | 0.25   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |       0.009 | 3/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |      -0.018 | 1/5       | 0.1875 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |       0.022 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |      -0.095 | 0/5       | 0.0625 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |      -0.085 | 2/5       | 0.3125 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |       0.027 | 3/5       | 0.3125 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |      -0.112 | 1/5       | 0.1875 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |      -0.098 | 1/5       | 0.125  |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.09  | 1/5       | 0.1875 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |      -0.042 | 2/5       | 0.4375 |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.048 | 1/5       | 0.3125 |