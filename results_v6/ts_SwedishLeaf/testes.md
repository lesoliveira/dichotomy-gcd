# Wilcoxon pareado — ts_SwedishLeaf

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.044 | 4/5       | 0.375  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.036 | 3/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.047 | 4/5       | 0.1875 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.02  | 3/5       | 1      |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.02  | 3/5       | 0.875  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.027 | 2/5       | 0.625  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.072 | 3/5       | 0.25   |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.056 | 4/5       | 0.4375 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.072 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.062 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.062 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.055 | 4/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.091 | 4/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.091 | 4/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.067 | 4/5       | 0.4375 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |      -2.4   | 1/5       | 0.25   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.007 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0.024 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.018 | 2/5       | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |      -5.6   | 0/5       | 0.25   |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.072 | 0/5       | 0.5    |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.018 | 1/5       | 0.75   |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.029 | 4/5       | 0.3125 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.04  | 1/5       | 0.625  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.032 | 2/5       | 0.5    |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.028 | 2/5       | 0.5    |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.028 | 4/5       | 0.4375 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.069 | 2/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |      -0.003 | 4/5       | 0.5625 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |      -0.203 | 0/5       | 0.125  |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.064 | 1/5       | 0.3125 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |      -0.139 | 1/5       | 0.25   |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |      -0.152 | 1/5       | 0.1875 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.128 | 1/5       | 0.25   |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.016 | 3/5       | 0.8125 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |       0.01  | 4/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.018 | 3/5       | 0.5    |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.011 | 3/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.022 | 3/5       | 0.5    |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |      -0.007 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |      -0.007 | 2/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |       0     | 3/5       | 0.875  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.048 | 4/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.032 | 3/5       | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.048 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |      -0.044 | 1/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |      -0.044 | 1/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |      -0.051 | 1/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |      -0.077 | 1/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |      -0.077 | 1/5       | 0.4375 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |      -0.101 | 1/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -1     | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0     | 1/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.016 | 1/5       | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.012 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |      -3.6   | 0/5       | 0.25   |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.08  | 0/5       | 0.25   |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |       0.011 | 1/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.033 | 4/5       | 0.125  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |       0.008 | 1/5       | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.056 | 3/5       | 0.625  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |       0.007 | 2/5       | 0.625  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |      -0.044 | 1/5       | 0.1875 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |       0.029 | 2/5       | 0.5    |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |      -0.072 | 1/5       | 0.375  |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |      -0.085 | 1/5       | 0.5    |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |       0.027 | 2/5       | 1      |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |      -0.112 | 2/5       | 0.3125 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |      -0.125 | 2/5       | 0.3125 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |      -0.101 | 2/5       | 0.3125 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.043 | 3/5       | 0.4375 |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.047 | 2/5       | 0.4375 |