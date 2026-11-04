# Wilcoxon pareado — omniglot_dinov2

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |  10 |       0.03  | 8/10      | 0.0293 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.04  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |  10 |       0.012 | 8/10      | 0.2637 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |  10 |       0.027 | 9/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.041 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |  10 |       0.013 | 8/10      | 0.0781 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |  10 |       0.039 | 7/10      | 0.1953 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.039 | 5/10      | 0.4492 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |  10 |       0.007 | 7/10      | 0.8457 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |  10 |       0.01  | 6/10      | 0.4922 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |  10 |       0.01  | 6/10      | 0.4922 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |  10 |       0.002 | 4/10      | 0.6953 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |  10 |       0.059 | 8/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.059 | 8/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |  10 |       0.034 | 8/10      | 0.0215 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |  10 |     -14.1   | 2/10      | 0.0098 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |  10 |       0.004 | 6/10      | 0.0312 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |  10 |       0     | 1/10      | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |  10 |       0.026 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |  10 |     -26.1   | 0/10      | 0.002  |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |  10 |      -0.171 | 0/10      | 0.0078 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |  10 |       0.016 | 7/10      | 0.0273 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |  10 |       0.027 | 8/10      | 0.0215 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |  10 |       0.047 | 7/10      | 0.0234 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |  10 |       0.054 | 8/10      | 0.0859 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |  10 |       0.001 | 4/10      | 0.9023 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |  10 |       0.003 | 4/10      | 0.7891 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |  10 |       0.006 | 5/10      | 0.9434 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |  10 |       0.04  | 9/10      | 0.0137 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |  10 |      -0.004 | 6/10      | 0.9414 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |  10 |       0.019 | 7/10      | 0.2871 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |  10 |      -0.023 | 4/10      | 0.5703 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |  10 |      -0.082 | 1/10      | 0.0098 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.125 | 0/10      | 0.002  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |  10 |       0.198 | 5/10      | 0.1641 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |  10 |       0.015 | 8/10      | 0.0195 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |  10 |       0.026 | 7/10      | 0.0664 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.036 | 7/10      | 0.0273 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |  10 |       0.008 | 7/10      | 0.5566 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |  10 |       0.018 | 5/10      | 0.1562 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.032 | 8/10      | 0.0195 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |  10 |       0.004 | 5/10      | 0.5801 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |  10 |       0.05  | 6/10      | 0.0996 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.05  | 6/10      | 0.2246 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |  10 |       0.018 | 5/10      | 0.5391 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |  10 |      -0.011 | 3/10      | 0.168  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |  10 |      -0.011 | 3/10      | 0.168  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |  10 |      -0.02  | 3/10      | 0.084  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |  10 |       0.002 | 5/10      | 0.9219 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.002 | 5/10      | 0.9219 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |  10 |      -0.023 | 5/10      | 0.375  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |  10 |      -7.7   | 2/10      | 0.1309 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |  10 |       0.004 | 4/10      | 0.6875 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |  10 |      -0.003 | 3/10      | 0.9375 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |  10 |       0.04  | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |  10 |     -46.7   | 0/10      | 0.002  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |  10 |      -0.03  | 0/10      | 0.0156 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |  10 |      -0.002 | 3/10      | 0.3594 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |  10 |       0.005 | 6/10      | 0.6758 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |  10 |      -0.013 | 3/10      | 0.3613 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |  10 |       0.005 | 6/10      | 0.8281 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |  10 |      -0.011 | 2/10      | 0.0312 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |  10 |      -0.031 | 2/10      | 0.0098 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |  10 |      -0.035 | 2/10      | 0.0391 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |  10 |      -0.058 | 2/10      | 0.0664 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |  10 |      -0.013 | 6/10      | 0.9004 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |  10 |      -0.021 | 2/10      | 0.207  |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |  10 |       0.008 | 7/10      | 0.2754 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |  10 |      -0.051 | 3/10      | 0.0645 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.094 | 0/10      | 0.002  |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |  10 |       0.229 | 8/10      | 0.0273 |
| dicotomia-logreg               | LR-MSP                             | auroc     |  10 |      -0.053 | 0/10      | 0.002  |