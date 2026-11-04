# Wilcoxon pareado — ts_NonInvasiveFetalECGThorax1

A_vence = nº de pares com A > B (para k_err, menor é melhor: dif. negativa favorece A).

| A                              | B                                  | métrica   |   n |   dif_média | A_vence   |      p |
|:-------------------------------|:-----------------------------------|:----------|----:|------------:|:----------|-------:|
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_all  |   5 |       0.096 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.103 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_all  |   5 |       0.112 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_old  |   5 |       0.102 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.117 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_old  |   5 |       0.126 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | test_new  |   5 |       0.089 | 3/5       | 0.3125 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.086 | 4/5       | 0.125  |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | test_new  |   5 |       0.094 | 4/5       | 0.1875 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | all       |   5 |       0.093 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.093 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | all       |   5 |       0.098 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K oráculo)              | new       |   5 |       0.113 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.113 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | new       |   5 |       0.099 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | SS-kmeans (K estimado)             | k_err     |   5 |      -1.8   | 1/5       | 0.4375 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_all  |   5 |       0.004 | 2/5       | 0.75   |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | test_new  |   5 |       0     | 3/5       | 0.875  |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | all       |   5 |       0.029 | 5/5       | 0.0625 |
| dicotomia-hgb + ruído          | dicotomia-hgb                      | k_est     |   5 |     -14.2   | 0/5       | 0.0625 |
| dicotomia-hgb + merge-back     | dicotomia-hgb                      | test_new  |   5 |      -0.069 | 0/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_all  |   5 |      -0.009 | 1/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_all  |   5 |       0.103 | 5/5       | 0.0625 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | test_new  |   5 |      -0.02  | 2/5       | 0.375  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | test_new  |   5 |       0.074 | 3/5       | 0.3125 |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | all       |   5 |      -0.018 | 0/5       | 0.0625 |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | all       |   5 |       0.079 | 4/5       | 0.125  |
| dicotomia-hgb + híbrido        | dicotomia-hgb + ruído              | new       |   5 |      -0.021 | 0/5       | 0.125  |
| dicotomia-hgb + híbrido        | SS-kmeans (K estimado)             | new       |   5 |       0.078 | 4/5       | 0.125  |
| dicotomia-hgb K auto + Ward    | kmeans (K oráculo)                 | acc       |   5 |       0.071 | 3/5       | 0.3125 |
| dicotomia-hgb K auto + Ward    | dicotomia-hgb (K auto)             | acc       |   5 |      -0.01  | 1/5       | 0.375  |
| dicotomia-hgb (K auto)         | kmeans (K oráculo)                 | acc       |   5 |       0.081 | 4/5       | 0.1875 |
| dicotomia-hgb (K auto)         | aglom. ward (K oráculo)            | acc       |   5 |       0.066 | 4/5       | 0.125  |
| dicotomia-hgb (K auto)         | NCA + kmeans (K oráculo)           | acc       |   5 |       0.413 | 5/5       | 0.0625 |
| dicotomia-hgb (K auto)         | kmeans (K silhueta)                | acc       |   5 |       0.187 | 3/5       | 0.3125 |
| dicotomia-hgb                  | LR-MSP                             | auroc     |   5 |      -0.019 | 2/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_all  |   5 |       0.082 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_all  |   5 |       0.088 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_all  |   5 |       0.097 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_old  |   5 |       0.079 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_old  |   5 |       0.093 | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_old  |   5 |       0.102 | 4/5       | 0.125  |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | test_new  |   5 |       0.086 | 4/5       | 0.3125 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | test_new  |   5 |       0.083 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | test_new  |   5 |       0.091 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | all       |   5 |       0.076 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | all       |   5 |       0.076 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | all       |   5 |       0.081 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | SS-kmeans (K oráculo)              | new       |   5 |       0.083 | 4/5       | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans + protótipos (K oráculo) | new       |   5 |       0.083 | 4/5       | 0.25   |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | new       |   5 |       0.069 | 4/5       | 0.1875 |
| dicotomia-logreg + ruído       | SS-kmeans (K estimado)             | k_err     |   5 |      -2.8   | 0/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_all  |   5 |       0.004 | 3/5       | 0.625  |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | test_new  |   5 |       0.017 | 2/5       | 0.5    |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | all       |   5 |       0.033 | 5/5       | 0.0625 |
| dicotomia-logreg + ruído       | dicotomia-logreg                   | k_est     |   5 |     -13.4   | 0/5       | 0.0625 |
| dicotomia-logreg + merge-back  | dicotomia-logreg                   | test_new  |   5 |      -0.031 | 1/5       | 0.3125 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_all  |   5 |      -0.013 | 1/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_all  |   5 |       0.084 | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | test_new  |   5 |      -0.029 | 0/5       | 0.25   |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | test_new  |   5 |       0.063 | 3/5       | 0.375  |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | all       |   5 |      -0.011 | 2/5       | 0.3125 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | all       |   5 |       0.07  | 5/5       | 0.0625 |
| dicotomia-logreg + híbrido     | dicotomia-logreg + ruído           | new       |   5 |       0.023 | 3/5       | 0.4375 |
| dicotomia-logreg + híbrido     | SS-kmeans (K estimado)             | new       |   5 |       0.091 | 4/5       | 0.125  |
| dicotomia-logreg K auto + Ward | kmeans (K oráculo)                 | acc       |   5 |       0.046 | 3/5       | 0.375  |
| dicotomia-logreg K auto + Ward | dicotomia-logreg (K auto)          | acc       |   5 |      -0.077 | 0/5       | 0.125  |
| dicotomia-logreg (K auto)      | kmeans (K oráculo)                 | acc       |   5 |       0.123 | 4/5       | 0.125  |
| dicotomia-logreg (K auto)      | aglom. ward (K oráculo)            | acc       |   5 |       0.108 | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | NCA + kmeans (K oráculo)           | acc       |   5 |       0.455 | 5/5       | 0.0625 |
| dicotomia-logreg (K auto)      | kmeans (K silhueta)                | acc       |   5 |       0.229 | 5/5       | 0.0625 |
| dicotomia-logreg               | LR-MSP                             | auroc     |   5 |      -0.053 | 1/5       | 0.125  |