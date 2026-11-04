## omniglot_hog
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

## omniglot_dinov2
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

## representação (test_all)
 | método                             |   omniglot_dinov2 − omniglot_hog |     p |
|:-----------------------------------|---------------------------------:|------:|
| SS-kmeans (K estimado)             |                            0.172 | 0.002 |
| SS-kmeans (K oráculo)              |                            0.176 | 0.002 |
| SS-kmeans + protótipos (K oráculo) |                            0.179 | 0.002 |
| dicotomia-hgb                      |                            0.141 | 0.002 |
| dicotomia-hgb + híbrido            |                            0.16  | 0.002 |
| dicotomia-hgb + merge-back         |                            0.123 | 0.002 |
| dicotomia-hgb + ruído              |                            0.144 | 0.002 |
| dicotomia-logreg                   |                            0.147 | 0.002 |
| dicotomia-logreg + híbrido         |                            0.148 | 0.002 |
| dicotomia-logreg + merge-back      |                            0.142 | 0.002 |
| dicotomia-logreg + ruído           |                            0.151 | 0.002 |
