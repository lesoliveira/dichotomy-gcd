# Wilcoxon pareado — omniglot_hog

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |  10 |       0.03  | 8/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.02  | 7/10      | 0.0703 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |  10 |       0.021 | 8/10      | 0.0273 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |  10 |       0.021 | 8/10      | 0.0371 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.009 | 7/10      | 0.1328 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |  10 |       0.014 | 6/10      | 0.1289 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |  10 |       0.058 | 8/10      | 0.0391 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.054 | 8/10      | 0.0684 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |  10 |       0.04  | 9/10      | 0.0371 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |  10 |      -0.009 | 5/10      | 0.4922 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |  10 |      -0.009 | 5/10      | 0.4922 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |  10 |      -0.004 | 5/10      | 0.6953 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |  10 |       0.059 | 8/10      | 0.084  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.059 | 8/10      | 0.084  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |  10 |       0.059 | 8/10      | 0.0488 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |  10 |     -16.5   | 1/10      | 0.043  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |  10 |       0     | 2/10      | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |  10 |       0.003 | 2/10      | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |  10 |       0.013 | 9/10      | 0.0039 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |  10 |     -18     | 0/10      | 0.002  |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |  10 |      -0.112 | 1/10      | 0.0078 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |  10 |       0.002 | 6/10      | 0.6328 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |  10 |       0.023 | 8/10      | 0.0117 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |  10 |       0.022 | 5/10      | 0.3594 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |  10 |       0.062 | 8/10      | 0.0078 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |  10 |      -0     | 5/10      | 0.8652 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |  10 |      -0.005 | 5/10      | 0.7129 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |  10 |       0.002 | 5/10      | 0.7695 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |  10 |       0.061 | 8/10      | 0.0078 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |  10 |      -0.018 | 5/10      | 0.4316 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |  10 |       0.033 | 6/10      | 0.2422 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |  10 |      -0.051 | 3/10      | 0.1289 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |  10 |      -0.072 | 2/10      | 0.0371 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.139 | 0/10      | 0.002  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |  10 |       0.075 | 7/10      | 0.4316 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |  10 |       0.007 | 6/10      | 0.5566 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |  10 |       0.02  | 9/10      | 0.0078 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.01  | 6/10      | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |  10 |       0.011 | 7/10      | 0.2871 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |  10 |       0.004 | 6/10      | 0.5371 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |      -0.009 | 2/10      | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |  10 |      -0.003 | 5/10      | 0.9434 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |  10 |       0.07  | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.066 | 9/10      | 0.0117 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |  10 |       0.052 | 9/10      | 0.0098 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |  10 |      -0.032 | 2/10      | 0.0195 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |  10 |      -0.032 | 2/10      | 0.0195 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |  10 |      -0.027 | 3/10      | 0.0488 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |  10 |       0.038 | 7/10      | 0.0996 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.038 | 7/10      | 0.0996 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |  10 |       0.038 | 8/10      | 0.0996 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |  10 |       0.1   | 7/10      | 0.6777 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |  10 |      -0     | 4/10      | 0.9375 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |  10 |       0     | 2/10      | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |  10 |       0.023 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |  10 |     -41.7   | 0/10      | 0.002  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |  10 |      -0.033 | 1/10      | 0.0078 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |  10 |      -0     | 3/10      | 1      |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |  10 |       0.01  | 7/10      | 0.2012 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |  10 |      -0.015 | 2/10      | 0.1406 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |  10 |       0.037 | 8/10      | 0.0605 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |  10 |       0.001 | 2/10      | 0.3125 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |  10 |      -0.026 | 3/10      | 0.0898 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |  10 |      -0.009 | 2/10      | 0.1152 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |  10 |       0.029 | 6/10      | 0.25   |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |  10 |      -0.051 | 2/10      | 0.0977 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |  10 |      -0.042 | 2/10      | 0.0195 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |  10 |      -0.009 | 5/10      | 0.7578 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |  10 |      -0.03  | 3/10      | 0.0781 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.097 | 0/10      | 0.002  |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |  10 |       0.117 | 7/10      | 0.1602 |
| dicotomia-logreg               | LR-MSP                             | auroc     |  10 |      -0.05  | 0/10      | 0.002  |