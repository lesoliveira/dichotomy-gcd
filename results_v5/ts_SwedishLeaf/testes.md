# Wilcoxon pareado — ts_SwedishLeaf

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.076 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.178 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.069 | 4/5       | 0.1875 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.027 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.207 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.013 | 1/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.136 | 4/5       | 0.375  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.144 | 4/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.136 | 4/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.154 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.154 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.159 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.203 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.203 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.229 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |      -8.2   | 0/5       | 0.0625 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.007 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.024 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.018 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |      -5.6   | 0/5       | 0.25   |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.072 | 0/5       | 0.5    |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.029 | 2/5       | 0.5    |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.04  | 3/5       | 0.5    |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.048 | 2/5       | 0.5625 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.088 | 2/5       | 0.625  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.05  | 1/5       | 0.25   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.109 | 4/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.112 | 1/5       | 0.125  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |       0.117 | 4/5       | 0.25   |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |       0.088 | 3/5       | 0.3125 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.027 | 1/5       | 0.625  |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |       0.115 | 4/5       | 0.625  |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |       0.021 | 4/5       | 0.625  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |       0.216 | 4/5       | 0.125  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.096 | 4/5       | 0.4375 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |       0.004 | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.051 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.153 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.044 | 3/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |      -0     | 1/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.18  | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |      -0.013 | 2/5       | 0.75   |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.112 | 3/5       | 0.5    |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.12  | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.112 | 3/5       | 0.375  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |       0.048 | 4/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.048 | 4/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |       0.052 | 3/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |       0.035 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.035 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |       0.061 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -6.8   | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0     | 1/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.016 | 1/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.012 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |      -3.6   | 0/5       | 0.25   |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.08  | 0/5       | 0.25   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0     | 2/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.044 | 3/5       | 0.25   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |      -0.024 | 1/5       | 0.5    |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.088 | 3/5       | 0.5    |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.017 | 1/5       | 0.375  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |       0.036 | 3/5       | 0.625  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |      -0.016 | 1/5       | 0.375  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |       0.045 | 3/5       | 0.6875 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |       0.077 | 4/5       | 0.3125 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.064 | 2/5       | 0.625  |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |       0.141 | 4/5       | 0.3125 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |       0.048 | 3/5       | 0.625  |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |       0.243 | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.123 | 4/5       | 0.4375 |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.053 | 2/5       | 0.3125 |