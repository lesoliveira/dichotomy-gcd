## omniglot_hog
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

## omniglot_dinov2
 | A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |  10 |       0.118 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.08  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |  10 |       0.101 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |  10 |       0.118 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.082 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |  10 |       0.102 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |  10 |       0.115 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.075 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |  10 |       0.098 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |  10 |       0.08  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |  10 |       0.08  | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |  10 |       0.076 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |  10 |       0.108 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.108 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |  10 |       0.102 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |  10 |     -15.8   | 2/10      | 0.1016 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |  10 |       0.004 | 6/10      | 0.0312 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |  10 |      -0.001 | 1/10      | 1      |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |  10 |       0.026 | 10/10     | 0.002  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |  10 |     -26.6   | 0/10      | 0.002  |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |  10 |      -0.174 | 0/10      | 0.0078 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |  10 |       0.007 | 7/10      | 0.1367 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |  10 |       0.108 | 10/10     | 0.002  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |  10 |       0.026 | 7/10      | 0.1875 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |  10 |       0.124 | 10/10     | 0.002  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |  10 |      -0.005 | 3/10      | 0.3223 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |  10 |       0.072 | 10/10     | 0.002  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |  10 |      -0.015 | 3/10      | 0.2754 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |  10 |       0.087 | 10/10     | 0.002  |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |  10 |      -0.004 | 5/10      | 0.9219 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |  10 |      -0.026 | 5/10      | 0.5371 |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |  10 |       0.022 | 6/10      | 0.4766 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |  10 |      -0.034 | 4/10      | 0.3223 |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.104 | 0/10      | 0.002  |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |  10 |       0.133 | 10/10     | 0.002  |
| dicotomia-hgb                  | LR-MSP                             | auroc     |  10 |       0.017 | 8/10      | 0.0195 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |  10 |       0.113 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |  10 |       0.075 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |  10 |       0.096 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |  10 |       0.109 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |  10 |       0.072 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |  10 |       0.092 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |  10 |       0.124 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |  10 |       0.084 | 8/10      | 0.0156 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |  10 |       0.107 | 9/10      | 0.0059 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |  10 |       0.057 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |  10 |       0.057 | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |  10 |       0.053 | 9/10      | 0.0039 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |  10 |       0.05  | 7/10      | 0.1934 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |  10 |       0.05  | 7/10      | 0.1934 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |  10 |       0.045 | 7/10      | 0.2324 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |  10 |      -8.5   | 4/10      | 0.1094 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |  10 |       0.004 | 4/10      | 0.6875 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |  10 |      -0.003 | 3/10      | 0.9375 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |  10 |       0.04  | 10/10     | 0.002  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |  10 |     -46.7   | 0/10      | 0.002  |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |  10 |      -0.03  | 0/10      | 0.0156 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |  10 |      -0.004 | 3/10      | 0.3164 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |  10 |       0.092 | 10/10     | 0.002  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |  10 |      -0.015 | 2/10      | 0.2383 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |  10 |       0.092 | 10/10     | 0.002  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |  10 |      -0.021 | 1/10      | 0.0039 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |  10 |       0.032 | 8/10      | 0.0137 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |  10 |      -0.06  | 1/10      | 0.0039 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |  10 |      -0.015 | 4/10      | 0.4316 |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |  10 |      -0.031 | 4/10      | 0.6523 |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |  10 |      -0.084 | 1/10      | 0.0059 |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |  10 |       0.053 | 9/10      | 0.0645 |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |  10 |      -0.003 | 4/10      | 0.748  |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |  10 |      -0.073 | 2/10      | 0.0195 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |  10 |       0.164 | 8/10      | 0.0195 |
| dicotomia-logreg               | LR-MSP                             | auroc     |  10 |      -0.05  | 0/10      | 0.002  | 

## representação (test_all)
 | método                             |   omniglot_dinov2 − omniglot_hog |      p |
|:-----------------------------------|---------------------------------:|-------:|
| SS-kmeans (K estimado)             |                            0.066 | 0.0039 |
| SS-kmeans (K oráculo)              |                            0.058 | 0.002  |
| SS-kmeans + protótipos (K oráculo) |                            0.086 | 0.002  |
| dicotomia-hgb                      |                            0.142 | 0.002  |
| dicotomia-hgb + híbrido            |                            0.151 | 0.002  |
| dicotomia-hgb + merge-back         |                            0.124 | 0.002  |
| dicotomia-hgb + ruído              |                            0.146 | 0.002  |
| dicotomia-logreg                   |                            0.147 | 0.002  |
| dicotomia-logreg + híbrido         |                            0.147 | 0.002  |
| dicotomia-logreg + merge-back      |                            0.142 | 0.002  |
| dicotomia-logreg + ruído           |                            0.151 | 0.002  |
