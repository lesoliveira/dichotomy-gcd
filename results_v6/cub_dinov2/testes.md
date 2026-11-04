# Wilcoxon pareado — cub_dinov2

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |  10 |       0.025 | 8/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.018 | 8/10      | 0.1055 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |  10 |       0.016 | 9/10      | 0.0195 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |  10 |       0.031 | 8/10      | 0.0176 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.029 | 8/10      | 0.0176 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |  10 |       0.021 | 7/10      | 0.1016 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |  10 |       0.004 | 4/10      | 0.9766 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |      -0.015 | 3/10      | 0.5371 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |  10 |      -0.002 | 5/10      | 0.9922 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |  10 |      -0.002 | 6/10      | 1      |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |  10 |      -0.002 | 6/10      | 1      |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |  10 |      -0.007 | 3/10      | 0.7695 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |  10 |      -0.047 | 1/10      | 0.0781 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |  10 |      -0.047 | 1/10      | 0.0781 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |  10 |      -0.041 | 3/10      | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |  10 |      -6.5   | 1/10      | 0.0234 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |  10 |       0.007 | 8/10      | 0.0156 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |  10 |       0.014 | 8/10      | 0.1172 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |  10 |       0.039 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |  10 |     -40.4   | 0/10      | 0.002  |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |  10 |      -0.027 | 3/10      | 0.1055 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |  10 |       0.005 | 6/10      | 0.0625 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |  10 |       0.021 | 9/10      | 0.0137 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |  10 |       0.014 | 5/10      | 0.3438 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |  10 |       0.012 | 7/10      | 0.625  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |  10 |       0.006 | 7/10      | 0.1172 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |  10 |      -0     | 5/10      | 0.4766 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |  10 |       0.022 | 6/10      | 0.1484 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |  10 |      -0.019 | 3/10      | 0.2656 |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |  10 |      -0.032 | 3/10      | 0.0645 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |  10 |       0.061 | 9/10      | 0.0273 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |  10 |      -0.092 | 1/10      | 0.0078 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |  10 |      -0.101 | 0/10      | 0.002  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.103 | 1/10      | 0.0059 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |  10 |       0.051 | 6/10      | 0.4316 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |  10 |      -0.017 | 4/10      | 0.1934 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |  10 |       0.034 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.027 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |  10 |       0.025 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |  10 |       0.037 | 8/10      | 0.0117 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.035 | 9/10      | 0.0059 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |  10 |       0.027 | 7/10      | 0.0254 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |  10 |       0.024 | 7/10      | 0.4434 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.005 | 4/10      | 0.9766 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |  10 |       0.018 | 6/10      | 0.4668 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |  10 |       0.003 | 6/10      | 0.791  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |  10 |       0.003 | 6/10      | 0.791  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |  10 |      -0.002 | 6/10      | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |  10 |      -0.028 | 3/10      | 0.2227 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |  10 |      -0.028 | 3/10      | 0.2227 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |  10 |      -0.022 | 5/10      | 0.416  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |  10 |      -6.5   | 2/10      | 0.0547 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |  10 |       0.013 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |  10 |       0.037 | 7/10      | 0.0156 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |  10 |       0.069 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |  10 |     -59.6   | 0/10      | 0.002  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |  10 |      -0.01  | 2/10      | 0.3281 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |  10 |       0.007 | 5/10      | 0.0625 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |  10 |       0.032 | 9/10      | 0.0039 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |  10 |       0.022 | 4/10      | 0.125  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |  10 |       0.04  | 7/10      | 0.1406 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |  10 |       0.004 | 4/10      | 0.418  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |  10 |       0.002 | 7/10      | 0.7695 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |  10 |       0.015 | 4/10      | 0.4258 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |  10 |      -0.007 | 4/10      | 0.7695 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |  10 |      -0.033 | 3/10      | 0.1113 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |  10 |       0.04  | 6/10      | 0.1289 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |  10 |      -0.073 | 2/10      | 0.0098 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |  10 |      -0.082 | 0/10      | 0.002  |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.084 | 2/10      | 0.0137 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |  10 |       0.07  | 6/10      | 0.2871 |
| dicotomia-logreg               | LR-MSP                             | auroc     |  10 |      -0.054 | 1/10      | 0.0039 |