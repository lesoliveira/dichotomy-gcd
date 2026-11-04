# Wilcoxon pareado — ts_Crop

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.08  | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.093 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.066 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.142 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.125 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.121 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.005 | 3/5       | 0.75   |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.055 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0     | 3/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.008 | 3/5       | 0.8125 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.008 | 3/5       | 0.8125 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.004 | 3/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.013 | 2/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.013 | 2/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.01  | 3/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |       0.6   | 2/5       | 0.75   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |      -0     | 1/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.005 | 1/5       | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.004 | 3/5       | 0.375  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |      -6.2   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |       0     | 1/5       | 1      |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.016 | 0/5       | 0.25   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.05  | 4/5       | 0.1875 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.015 | 2/5       | 0.6875 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |      -0.015 | 2/5       | 0.6875 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.016 | 1/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |      -0.011 | 2/5       | 0.625  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.035 | 1/5       | 0.25   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |      -0.025 | 2/5       | 0.5    |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |       0.015 | 3/5       | 0.8125 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.103 | 0/5       | 0.0625 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |       0.118 | 5/5       | 0.0625 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |       0.118 | 5/5       | 0.0625 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |       0.242 | 5/5       | 0.0625 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.182 | 5/5       | 0.0625 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |       0.021 | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.023 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.036 | 4/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.009 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |       0.004 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |      -0.012 | 3/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |      -0.017 | 2/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.045 | 4/5       | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.095 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.04  | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |      -0.021 | 2/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |      -0.021 | 2/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |      -0.024 | 2/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |       0.007 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.007 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |       0.003 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -2.6   | 1/5       | 0.4375 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |      -0.005 | 0/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |      -0.005 | 0/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.003 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |      -5     | 0/5       | 0.125  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.08  | 0/5       | 0.125  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0.011 | 3/5       | 0.5    |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.02  | 2/5       | 1      |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |      -0.005 | 1/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.035 | 4/5       | 0.5625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.013 | 1/5       | 0.1875 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |      -0.037 | 0/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |      -0.017 | 1/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |      -0.013 | 2/5       | 0.625  |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |      -0.01  | 2/5       | 0.8125 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.072 | 1/5       | 0.125  |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |       0.062 | 3/5       | 0.3125 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |       0.062 | 4/5       | 0.3125 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |       0.185 | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.125 | 4/5       | 0.125  |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.052 | 1/5       | 0.3125 |