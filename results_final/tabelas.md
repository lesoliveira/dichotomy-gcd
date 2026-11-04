# Tabelas finais (critério conservador)

## Wilcoxon pareado: proposto vs. cada comparação no seu melhor pré-processamento

Para k_err, menor é melhor; `proposto_melhor` já conta os pares a favor do proposto.

| tabela     | métrica   | comparação                                    | grupo    |   n |     dif | proposto_melhor   |      p |
|:-----------|:----------|:----------------------------------------------|:---------|----:|--------:|:------------------|-------:|
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | todos    |  50 |   0.041 | 44/50             | 0      |
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | sem CUB  |  40 |   0.048 | 35/40             | 0      |
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | imagens  |  30 |   0.016 | 25/30             | 0.0006 |
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | séries   |  20 |   0.079 | 19/20             | 0.0001 |
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | Omniglot |  20 |   0.017 | 16/20             | 0.008  |
| gcd        | test_all  | proposto − SS-kmeans (K estimado)             | CUB      |  10 |   0.016 | 9/10              | 0.0195 |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | todos    |  50 |   0.045 | 42/50             | 0      |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | sem CUB  |  40 |   0.05  | 34/40             | 0      |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | imagens  |  30 |   0.029 | 24/30             | 0.0001 |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | séries   |  20 |   0.069 | 18/20             | 0.0008 |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | Omniglot |  20 |   0.031 | 16/20             | 0.0017 |
| gcd        | test_all  | proposto − SS-kmeans (K oráculo)              | CUB      |  10 |   0.025 | 8/10              | 0.0195 |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | todos    |  50 |   0.043 | 43/50             | 0      |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | sem CUB  |  40 |   0.049 | 35/40             | 0      |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | imagens  |  30 |   0.026 | 25/30             | 0.0002 |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | séries   |  20 |   0.067 | 18/20             | 0.001  |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | Omniglot |  20 |   0.031 | 17/20             | 0.0011 |
| gcd        | test_all  | proposto − SS-kmeans + protótipos (K oráculo) | CUB      |  10 |   0.018 | 8/10              | 0.1055 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | todos    |  50 |   0.02  | 29/50             | 0.0152 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | sem CUB  |  40 |   0.032 | 28/40             | 0.0002 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | imagens  |  30 |  -0     | 13/30             | 0.9181 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | séries   |  20 |   0.051 | 16/20             | 0.0014 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | Omniglot |  20 |   0.014 | 12/20             | 0.0521 |
| gcd        | test_all  | proposto − dicotomia-euclid + ruído           | CUB      |  10 |  -0.029 | 1/10              | 0.0039 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | todos    |  50 |   0.033 | 36/50             | 0.0059 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | sem CUB  |  40 |   0.042 | 31/40             | 0.0013 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | imagens  |  30 |   0.016 | 21/30             | 0.2942 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | séries   |  20 |   0.059 | 15/20             | 0.0055 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | Omniglot |  20 |   0.024 | 16/20             | 0.1043 |
| gcd        | test_new  | proposto − SS-kmeans (K estimado)             | CUB      |  10 |  -0.002 | 5/10              | 0.9922 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | todos    |  50 |   0.034 | 30/50             | 0.0075 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | sem CUB  |  40 |   0.041 | 26/40             | 0.0032 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | imagens  |  30 |   0.034 | 20/30             | 0.0361 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | séries   |  20 |   0.033 | 10/20             | 0.1251 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | Omniglot |  20 |   0.05  | 16/20             | 0.0112 |
| gcd        | test_new  | proposto − SS-kmeans (K oráculo)              | CUB      |  10 |   0.004 | 4/10              | 0.9766 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | todos    |  50 |   0.027 | 27/50             | 0.0811 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | sem CUB  |  40 |   0.037 | 24/40             | 0.0203 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | imagens  |  30 |   0.027 | 16/30             | 0.1904 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | séries   |  20 |   0.027 | 11/20             | 0.2272 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | Omniglot |  20 |   0.047 | 13/20             | 0.0327 |
| gcd        | test_new  | proposto − SS-kmeans + protótipos (K oráculo) | CUB      |  10 |  -0.015 | 3/10              | 0.5371 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | todos    |  50 |   0.024 | 32/50             | 0.0642 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | sem CUB  |  40 |   0.044 | 29/40             | 0.0032 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | imagens  |  30 |   0.005 | 16/30             | 0.7951 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | séries   |  20 |   0.051 | 16/20             | 0.0019 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | Omniglot |  20 |   0.037 | 13/20             | 0.1614 |
| gcd        | test_new  | proposto − dicotomia-euclid + ruído           | CUB      |  10 |  -0.058 | 3/10              | 0.1289 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | todos    |  50 |   0.02  | 29/50             | 0.0197 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | sem CUB  |  40 |   0.027 | 26/40             | 0.0078 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | imagens  |  30 |  -0.003 | 12/30             | 0.8451 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | séries   |  20 |   0.054 | 17/20             | 0.0015 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | Omniglot |  20 |  -0     | 9/20              | 0.9563 |
| gcd        | all       | proposto − SS-kmeans (K estimado)             | CUB      |  10 |  -0.007 | 3/10              | 0.7695 |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | todos    |  50 |   0.018 | 32/50             | 0.0233 |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | sem CUB  |  40 |   0.024 | 26/40             | 0.0124 |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | imagens  |  30 |   0     | 17/30             | 0.9344 |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | séries   |  20 |   0.046 | 15/20             | 0.0051 |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | Omniglot |  20 |   0.001 | 11/20             | 1      |
| gcd        | all       | proposto − SS-kmeans (K oráculo)              | CUB      |  10 |  -0.002 | 6/10              | 1      |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | todos    |  50 |   0.018 | 32/50             | 0.0233 |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | sem CUB  |  40 |   0.024 | 26/40             | 0.0124 |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | imagens  |  30 |   0     | 17/30             | 0.9344 |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | séries   |  20 |   0.046 | 15/20             | 0.0051 |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | Omniglot |  20 |   0.001 | 11/20             | 1      |
| gcd        | all       | proposto − SS-kmeans + protótipos (K oráculo) | CUB      |  10 |  -0.002 | 6/10              | 1      |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | todos    |  50 |   0.029 | 31/50             | 0.0054 |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | sem CUB  |  40 |   0.041 | 30/40             | 0.0001 |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | imagens  |  30 |   0.003 | 14/30             | 0.805  |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | séries   |  20 |   0.067 | 17/20             | 0.0007 |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | Omniglot |  20 |   0.016 | 13/20             | 0.0826 |
| gcd        | all       | proposto − dicotomia-euclid + ruído           | CUB      |  10 |  -0.023 | 1/10              | 0.0195 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | todos    |  50 |   0.017 | 29/50             | 0.1793 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | sem CUB  |  40 |   0.031 | 26/40             | 0.0311 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | imagens  |  30 |   0.018 | 18/30             | 0.1598 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | séries   |  20 |   0.015 | 11/20             | 0.5256 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | Omniglot |  20 |   0.047 | 15/20             | 0.0055 |
| gcd        | new       | proposto − SS-kmeans (K estimado)             | CUB      |  10 |  -0.041 | 3/10              | 0.0625 |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | todos    |  50 |   0.018 | 26/50             | 0.2815 |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | sem CUB  |  40 |   0.034 | 25/40             | 0.0285 |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | imagens  |  30 |   0.024 | 17/30             | 0.2369 |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | séries   |  20 |   0.009 | 9/20              | 0.8276 |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | Omniglot |  20 |   0.059 | 16/20             | 0.004  |
| gcd        | new       | proposto − SS-kmeans (K oráculo)              | CUB      |  10 |  -0.047 | 1/10              | 0.0781 |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | todos    |  50 |   0.018 | 26/50             | 0.2815 |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | sem CUB  |  40 |   0.034 | 25/40             | 0.0285 |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | imagens  |  30 |   0.024 | 17/30             | 0.2369 |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | séries   |  20 |   0.009 | 9/20              | 0.8276 |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | Omniglot |  20 |   0.059 | 16/20             | 0.004  |
| gcd        | new       | proposto − SS-kmeans + protótipos (K oráculo) | CUB      |  10 |  -0.047 | 1/10              | 0.0781 |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | todos    |  50 |   0.09  | 39/50             | 0      |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | sem CUB  |  40 |   0.117 | 33/40             | 0      |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | imagens  |  30 |   0.092 | 25/30             | 0.0002 |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | séries   |  20 |   0.086 | 14/20             | 0.0192 |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | Omniglot |  20 |   0.147 | 19/20             | 0.0001 |
| gcd        | new       | proposto − dicotomia-euclid + ruído           | CUB      |  10 |  -0.018 | 6/10              | 0.9414 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | todos    |  50 |  -7.26  | 32/50             | 0.0008 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | sem CUB  |  40 |  -7.45  | 23/40             | 0.0101 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | imagens  |  30 | -12.667 | 26/30             | 0.0002 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | séries   |  20 |   0.85  | 6/20              | 0.5692 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | Omniglot |  20 | -15.75  | 17/20             | 0.0023 |
| gcd        | k_err     | proposto − SS-kmeans (K estimado)             | CUB      |  10 |  -6.5   | 9/10              | 0.0234 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | todos    |  50 |  -2.64  | 26/50             | 0.2048 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | sem CUB  |  40 |  -3     | 22/40             | 0.2029 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | imagens  |  30 |  -2.667 | 14/30             | 0.4872 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | séries   |  20 |  -2.6   | 12/20             | 0.1564 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | Omniglot |  20 |  -3.4   | 10/20             | 0.4995 |
| gcd        | k_err     | proposto − dicotomia-euclid + ruído           | CUB      |  10 |  -1.2   | 4/10              | 0.7852 |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | todos    |  50 |  -0.053 | 17/50             | 0.002  |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | sem CUB  |  40 |  -0.043 | 16/40             | 0.0395 |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | imagens  |  30 |  -0.055 | 8/30              | 0.0048 |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | séries   |  20 |  -0.05  | 9/20              | 0.2122 |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | Omniglot |  20 |  -0.037 | 7/20              | 0.1119 |
| descoberta | acc       | proposto − kmeans (K oráculo)                 | CUB      |  10 |  -0.092 | 1/10              | 0.0078 |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | todos    |  50 |  -0.074 | 7/50              | 0      |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | sem CUB  |  40 |  -0.067 | 7/40              | 0.0002 |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | imagens  |  30 |  -0.085 | 3/30              | 0      |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | séries   |  20 |  -0.058 | 4/20              | 0.0463 |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | Omniglot |  20 |  -0.077 | 3/20              | 0.0011 |
| descoberta | acc       | proposto − aglom. ward (K oráculo)            | CUB      |  10 |  -0.101 | 0/10              | 0.002  |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | todos    |  50 |  -0.101 | 8/50              | 0      |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | sem CUB  |  40 |  -0.096 | 8/40              | 0      |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | imagens  |  30 |  -0.131 | 0/30              | 0      |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | séries   |  20 |  -0.055 | 8/20              | 0.1031 |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | Omniglot |  20 |  -0.138 | 0/20              | 0.0001 |
| descoberta | acc       | proposto − NCA + kmeans (K oráculo)           | CUB      |  10 |  -0.119 | 0/10              | 0.002  |
| descoberta | acc       | proposto − kmeans (K silhueta)                | todos    |  50 |   0.064 | 31/50             | 0.0317 |
| descoberta | acc       | proposto − kmeans (K silhueta)                | sem CUB  |  40 |   0.08  | 27/40             | 0.0127 |
| descoberta | acc       | proposto − kmeans (K silhueta)                | imagens  |  30 |   0.07  | 21/30             | 0.0417 |
| descoberta | acc       | proposto − kmeans (K silhueta)                | séries   |  20 |   0.056 | 10/20             | 0.2179 |
| descoberta | acc       | proposto − kmeans (K silhueta)                | Omniglot |  20 |   0.104 | 17/20             | 0.0137 |
| descoberta | acc       | proposto − kmeans (K silhueta)                | CUB      |  10 |   0     | 4/10              | 0.6074 |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | todos    |  50 |   0.102 | 39/50             | 0      |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | sem CUB  |  40 |   0.131 | 35/40             | 0      |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | imagens  |  30 |   0.082 | 22/30             | 0.0009 |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | séries   |  20 |   0.133 | 17/20             | 0.0005 |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | Omniglot |  20 |   0.128 | 18/20             | 0.0002 |
| descoberta | acc       | proposto − dicotomia-euclid (K auto)          | CUB      |  10 |  -0.011 | 4/10              | 0.4258 |
| deteccao   | auroc     | proposto − LR-MSP                             | todos    |  50 |   0     | 28/50             | 0.6186 |
| deteccao   | auroc     | proposto − LR-MSP                             | sem CUB  |  40 |   0.005 | 24/40             | 0.2016 |
| deteccao   | auroc     | proposto − LR-MSP                             | imagens  |  30 |   0.001 | 18/30             | 0.5561 |
| deteccao   | auroc     | proposto − LR-MSP                             | séries   |  20 |  -0     | 10/20             | 1      |
| deteccao   | auroc     | proposto − LR-MSP                             | Omniglot |  20 |   0.01  | 14/20             | 0.0637 |
| deteccao   | auroc     | proposto − LR-MSP                             | CUB      |  10 |  -0.017 | 4/10              | 0.1934 |
| deteccao   | auroc     | proposto − 1NN-dist                           | todos    |  50 |   0.082 | 45/50             | 0      |
| deteccao   | auroc     | proposto − 1NN-dist                           | sem CUB  |  40 |   0.096 | 37/40             | 0      |
| deteccao   | auroc     | proposto − 1NN-dist                           | imagens  |  30 |   0.097 | 28/30             | 0      |
| deteccao   | auroc     | proposto − 1NN-dist                           | séries   |  20 |   0.06  | 17/20             | 0.0017 |
| deteccao   | auroc     | proposto − 1NN-dist                           | Omniglot |  20 |   0.132 | 20/20             | 0      |
| deteccao   | auroc     | proposto − 1NN-dist                           | CUB      |  10 |   0.026 | 8/10              | 0.0645 |
| deteccao   | auroc     | proposto − centroid-dist                      | todos    |  50 |   0.092 | 40/50             | 0      |
| deteccao   | auroc     | proposto − centroid-dist                      | sem CUB  |  40 |   0.115 | 37/40             | 0      |
| deteccao   | auroc     | proposto − centroid-dist                      | imagens  |  30 |   0.092 | 23/30             | 0      |
| deteccao   | auroc     | proposto − centroid-dist                      | séries   |  20 |   0.092 | 17/20             | 0      |
| deteccao   | auroc     | proposto − centroid-dist                      | Omniglot |  20 |   0.137 | 20/20             | 0      |
| deteccao   | auroc     | proposto − centroid-dist                      | CUB      |  10 |   0.003 | 3/10              | 0.9219 |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | todos    |  50 |   0.093 | 46/50             | 0      |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | sem CUB  |  40 |   0.111 | 38/40             | 0      |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | imagens  |  30 |   0.1   | 28/30             | 0      |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | séries   |  20 |   0.083 | 18/20             | 0      |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | Omniglot |  20 |   0.139 | 20/20             | 0      |
| deteccao   | auroc     | proposto − dicotomia-euclid                   | CUB      |  10 |   0.021 | 8/10              | 0.0371 |

## Médias por conjunto

| tabela     | métrica   | método                             |   omniglot_dinov2 |   omniglot_hog |   cub_dinov2 |   ts_ShapesAll |   ts_NonInvasiveFetalECGThorax1 |   ts_Crop |   ts_SwedishLeaf |
|:-----------|:----------|:-----------------------------------|------------------:|---------------:|-------------:|---------------:|--------------------------------:|----------:|-----------------:|
| gcd        | test_all  | dicotomia-hgb + ruído (proposto)   |             0.755 |          0.609 |        0.802 |          0.794 |                           0.781 |     0.527 |            0.709 |
| gcd        | test_all  | SS-kmeans (K estimado)             |             0.742 |          0.588 |        0.786 |          0.703 |                           0.669 |     0.461 |            0.662 |
| gcd        | test_all  | SS-kmeans (K oráculo)              |             0.724 |          0.579 |        0.777 |          0.695 |                           0.684 |     0.489 |            0.665 |
| gcd        | test_all  | SS-kmeans + protótipos (K oráculo) |             0.714 |          0.589 |        0.784 |          0.699 |                           0.697 |     0.473 |            0.673 |
| gcd        | test_all  | dicotomia-euclid + ruído           |             0.747 |          0.59  |        0.83  |          0.739 |                           0.717 |     0.477 |            0.673 |
| gcd        | test_new  | dicotomia-hgb + ruído (proposto)   |             0.655 |          0.492 |        0.718 |          0.708 |                           0.723 |     0.49  |            0.608 |
| gcd        | test_new  | SS-kmeans (K estimado)             |             0.646 |          0.452 |        0.72  |          0.638 |                           0.629 |     0.49  |            0.536 |
| gcd        | test_new  | SS-kmeans (K oráculo)              |             0.614 |          0.434 |        0.714 |          0.646 |                           0.669 |     0.545 |            0.536 |
| gcd        | test_new  | SS-kmeans + protótipos (K oráculo) |             0.614 |          0.438 |        0.733 |          0.646 |                           0.703 |     0.52  |            0.552 |
| gcd        | test_new  | dicotomia-euclid + ruído           |             0.644 |          0.429 |        0.776 |          0.642 |                           0.66  |     0.455 |            0.568 |
| gcd        | all       | dicotomia-hgb + ruído (proposto)   |             0.705 |          0.546 |        0.757 |          0.739 |                           0.746 |     0.413 |            0.717 |
| gcd        | all       | SS-kmeans (K estimado)             |             0.701 |          0.55  |        0.764 |          0.678 |                           0.649 |     0.411 |            0.662 |
| gcd        | all       | SS-kmeans (K oráculo)              |             0.693 |          0.555 |        0.759 |          0.682 |                           0.662 |     0.434 |            0.655 |
| gcd        | all       | SS-kmeans + protótipos (K oráculo) |             0.693 |          0.555 |        0.759 |          0.682 |                           0.662 |     0.434 |            0.655 |
| gcd        | all       | dicotomia-euclid + ruído           |             0.67  |          0.549 |        0.78  |          0.658 |                           0.661 |     0.43  |            0.6   |
| gcd        | new       | dicotomia-hgb + ruído (proposto)   |             0.615 |          0.444 |        0.654 |          0.639 |                           0.713 |     0.393 |            0.672 |
| gcd        | new       | SS-kmeans (K estimado)             |             0.58  |          0.385 |        0.694 |          0.635 |                           0.614 |     0.503 |            0.605 |
| gcd        | new       | SS-kmeans (K oráculo)              |             0.555 |          0.385 |        0.7   |          0.643 |                           0.671 |     0.487 |            0.581 |
| gcd        | new       | SS-kmeans + protótipos (K oráculo) |             0.555 |          0.385 |        0.7   |          0.643 |                           0.671 |     0.487 |            0.581 |
| gcd        | new       | dicotomia-euclid + ruído           |             0.463 |          0.302 |        0.672 |          0.524 |                           0.599 |     0.465 |            0.485 |
| gcd        | k_err     | dicotomia-hgb + ruído (proposto)   |             7.5   |         18.1   |        6.1   |         10     |                           3.6   |     5.8   |            1     |
| gcd        | k_err     | SS-kmeans (K estimado)             |            22.5   |         34.6   |       12.6   |          3.4   |                           5     |     5.2   |            3.4   |
| gcd        | k_err     | dicotomia-euclid + ruído           |            24.7   |          7.7   |        7.3   |         13.4   |                           2.6   |    12     |            2.8   |
| descoberta | acc       | dicotomia-hgb (K auto) (proposto)  |             0.745 |          0.56  |        0.736 |          0.711 |                           0.768 |     0.56  |            0.608 |
| descoberta | acc       | kmeans (K oráculo)                 |             0.768 |          0.611 |        0.828 |          0.754 |                           0.73  |     0.615 |            0.747 |
| descoberta | acc       | aglom. ward (K oráculo)            |             0.826 |          0.632 |        0.837 |          0.771 |                           0.746 |     0.602 |            0.76  |
| descoberta | acc       | NCA + kmeans (K oráculo)           |             0.87  |          0.71  |        0.855 |          0.809 |                           0.73  |     0.593 |            0.736 |
| descoberta | acc       | kmeans (K silhueta)                |             0.611 |          0.485 |        0.736 |          0.706 |                           0.581 |     0.545 |            0.592 |
| descoberta | acc       | dicotomia-euclid (K auto)          |             0.606 |          0.442 |        0.747 |          0.583 |                           0.641 |     0.555 |            0.336 |
| deteccao   | auroc     | dicotomia-hgb (proposto)           |             0.877 |          0.803 |        0.825 |          0.916 |                           0.885 |     0.683 |            0.859 |
| deteccao   | auroc     | LR-MSP                             |             0.862 |          0.797 |        0.843 |          0.923 |                           0.904 |     0.662 |            0.855 |
| deteccao   | auroc     | 1NN-dist                           |             0.774 |          0.642 |        0.799 |          0.888 |                           0.805 |     0.693 |            0.718 |
| deteccao   | auroc     | centroid-dist                      |             0.771 |          0.636 |        0.823 |          0.811 |                           0.78  |     0.674 |            0.709 |
| deteccao   | auroc     | dicotomia-euclid                   |             0.773 |          0.628 |        0.805 |          0.841 |                           0.796 |     0.676 |            0.699 |

## Pré-processamento escolhido para cada comparação

| tabela     | métrica   | método                             | omniglot_dinov2_prep   | omniglot_hog_prep   | cub_dinov2_prep   | ts_ShapesAll_prep   | ts_NonInvasiveFetalECGThorax1_prep   | ts_Crop_prep   | ts_SwedishLeaf_prep   |
|:-----------|:----------|:-----------------------------------|:-----------------------|:--------------------|:------------------|:--------------------|:-------------------------------------|:---------------|:----------------------|
| gcd        | test_all  | SS-kmeans (K estimado)             | whiten                 | sem whiten          | sem whiten        | whiten              | whiten                               | whiten         | sem whiten            |
| gcd        | test_all  | SS-kmeans (K oráculo)              | whiten                 | sem whiten          | sem whiten        | whiten              | whiten                               | sem whiten     | sem whiten            |
| gcd        | test_all  | SS-kmeans + protótipos (K oráculo) | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | test_all  | dicotomia-euclid + ruído           | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | test_new  | SS-kmeans (K estimado)             | whiten                 | sem whiten          | sem whiten        | whiten              | whiten                               | whiten         | sem whiten            |
| gcd        | test_new  | SS-kmeans (K oráculo)              | whiten                 | sem whiten          | sem whiten        | sem whiten          | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | test_new  | SS-kmeans + protótipos (K oráculo) | whiten                 | sem whiten          | sem whiten        | sem whiten          | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | test_new  | dicotomia-euclid + ruído           | whiten                 | whiten              | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | all       | SS-kmeans (K estimado)             | whiten                 | sem whiten          | sem whiten        | whiten              | whiten                               | sem whiten     | sem whiten            |
| gcd        | all       | SS-kmeans (K oráculo)              | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | all       | SS-kmeans + protótipos (K oráculo) | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | all       | dicotomia-euclid + ruído           | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | new       | SS-kmeans (K estimado)             | whiten                 | sem whiten          | sem whiten        | whiten              | whiten                               | sem whiten     | sem whiten            |
| gcd        | new       | SS-kmeans (K oráculo)              | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | new       | SS-kmeans + protótipos (K oráculo) | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | new       | dicotomia-euclid + ruído           | sem whiten             | sem whiten          | sem whiten        | sem whiten          | sem whiten                           | sem whiten     | sem whiten            |
| gcd        | k_err     | SS-kmeans (K estimado)             | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | whiten         | sem whiten            |
| gcd        | k_err     | dicotomia-euclid + ruído           | whiten                 | sem whiten          | whiten            | sem whiten          | whiten                               | sem whiten     | sem whiten            |
| descoberta | acc       | kmeans (K oráculo)                 | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| descoberta | acc       | aglom. ward (K oráculo)            | whiten                 | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| descoberta | acc       | NCA + kmeans (K oráculo)           | whiten                 | whiten              | whiten            | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| descoberta | acc       | kmeans (K silhueta)                | sem whiten             | sem whiten          | whiten            | whiten              | whiten                               | sem whiten     | sem whiten            |
| descoberta | acc       | dicotomia-euclid (K auto)          | sem whiten             | sem whiten          | sem whiten        | sem whiten          | sem whiten                           | sem whiten     | sem whiten            |
| deteccao   | auroc     | LR-MSP                             | whiten                 | whiten              | sem whiten        | whiten              | whiten                               | whiten         | whiten                |
| deteccao   | auroc     | 1NN-dist                           | sem whiten             | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| deteccao   | auroc     | centroid-dist                      | sem whiten             | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |
| deteccao   | auroc     | dicotomia-euclid                   | sem whiten             | sem whiten          | sem whiten        | whiten              | sem whiten                           | sem whiten     | sem whiten            |