# Wilcoxon pareado — omniglot_hog

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |  10 |       0.061 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.075 | 9/10      | 0.0039 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |  10 |       0.039 | 9/10      | 0.0039 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |  10 |       0.038 | 9/10      | 0.0078 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.066 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |  10 |       0.026 | 9/10      | 0.0215 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |  10 |       0.128 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.104 | 9/10      | 0.0059 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |  10 |       0.08  | 9/10      | 0.0098 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |  10 |       0.015 | 6/10      | 0.1055 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |  10 |       0.015 | 6/10      | 0.1055 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |  10 |       0.028 | 7/10      | 0.0254 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |  10 |       0.12  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.12  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |  10 |       0.111 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |  10 |     -36.8   | 1/10      | 0.0273 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |  10 |       0     | 2/10      | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |  10 |       0.003 | 2/10      | 0.5    |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |  10 |       0.013 | 9/10      | 0.0039 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |  10 |     -18     | 0/10      | 0.002  |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |  10 |      -0.112 | 1/10      | 0.0078 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |  10 |      -0     | 5/10      | 0.9844 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |  10 |       0.039 | 10/10     | 0.002  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |  10 |       0.019 | 6/10      | 0.3008 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |  10 |       0.099 | 10/10     | 0.002  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |  10 |       0     | 5/10      | 0.9023 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |  10 |       0.028 | 9/10      | 0.0039 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |  10 |       0.006 | 5/10      | 0.7695 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |  10 |       0.117 | 10/10     | 0.002  |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |  10 |      -0.004 | 7/10      | 0.7695 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |  10 |      -0.005 | 4/10      | 0.6953 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |  10 |       0.001 | 6/10      | 0.9219 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |  10 |      -0.006 | 6/10      | 1      |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.15  | 0/10      | 0.0039 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |  10 |       0.218 | 9/10      | 0.0195 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |  10 |       0.006 | 6/10      | 0.5566 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |  10 |       0.051 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.065 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |  10 |       0.029 | 9/10      | 0.0137 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |  10 |       0.021 | 7/10      | 0.0352 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.049 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |  10 |       0.009 | 6/10      | 0.2891 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |  10 |       0.138 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.114 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |  10 |       0.09  | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |  10 |      -0.007 | 4/10      | 0.6523 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |  10 |      -0.007 | 4/10      | 0.6523 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |  10 |       0.006 | 5/10      | 1      |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |  10 |       0.099 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.099 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |  10 |       0.091 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |  10 |     -20.2   | 4/10      | 0.3008 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |  10 |      -0     | 4/10      | 0.9375 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |  10 |       0     | 2/10      | 1      |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |  10 |       0.023 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |  10 |     -41.7   | 0/10      | 0.002  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |  10 |      -0.033 | 1/10      | 0.0078 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |  10 |       0     | 4/10      | 0.8008 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |  10 |       0.029 | 9/10      | 0.0137 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |  10 |      -0.028 | 1/10      | 0.0586 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |  10 |       0.062 | 9/10      | 0.0137 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |  10 |      -0.007 | 4/10      | 0.084  |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |  10 |      -0.001 | 4/10      | 0.6953 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |  10 |      -0.021 | 2/10      | 0.0488 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |  10 |       0.069 | 10/10     | 0.002  |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |  10 |      -0.017 | 5/10      | 0.334  |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |  10 |      -0.06  | 1/10      | 0.0078 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |  10 |       0.043 | 7/10      | 0.1055 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |  10 |       0.036 | 7/10      | 0.2754 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.108 | 1/10      | 0.0039 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |  10 |       0.26  | 9/10      | 0.0137 |
| dicotomia-logreg               | LR-MSP                             | auroc     |  10 |      -0.051 | 0/10      | 0.002  |