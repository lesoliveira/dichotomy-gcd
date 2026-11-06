# Sensitivity to the number of novel classes K

Mean over seeds (and near/far for Omniglot and CUB). Accuracy in %.


## Omniglot · DINOv2

|                                      |   K̂ |   |K̂−K| |   test all |   test new |   AUROC |
|:-------------------------------------|-----:|---------:|-----------:|-----------:|--------:|
| ('SS-kmeans (K estimado)', 0)        | 24.4 |     24.4 |       85.2 |      nan   |   nan   |
| ('SS-kmeans (K estimado)', 5)        | 32.5 |     27.5 |       79.7 |       52   |   nan   |
| ('SS-kmeans (K estimado)', 10)       | 37.4 |     27.4 |       78.1 |       57.6 |   nan   |
| ('SS-kmeans (K estimado)', 20)       | 42.5 |     22.5 |       74.2 |       64.6 |   nan   |
| ('SS-kmeans (K estimado)', 40)       | 55.3 |     19.7 |       67.1 |       55.9 |   nan   |
| ('SimGCD raso (K da dicotomia)', 0)  | 14.2 |     14.2 |       86.8 |      nan   |   nan   |
| ('SimGCD raso (K da dicotomia)', 5)  | 17   |     12   |       86.7 |       74   |   nan   |
| ('SimGCD raso (K da dicotomia)', 10) | 23.8 |     13.8 |       85.7 |       74   |   nan   |
| ('SimGCD raso (K da dicotomia)', 20) | 26.9 |      7.5 |       85.2 |       75.1 |   nan   |
| ('SimGCD raso (K da dicotomia)', 40) | 49.6 |     10.8 |       82.9 |       74.6 |   nan   |
| ('SimGCD raso (K estimado)', 0)      | 16.6 |     16.6 |       86.9 |      nan   |   nan   |
| ('SimGCD raso (K estimado)', 5)      | 21.9 |     17.5 |       84.5 |       67.2 |   nan   |
| ('SimGCD raso (K estimado)', 10)     | 24.3 |     15.5 |       86   |       74.2 |   nan   |
| ('SimGCD raso (K estimado)', 20)     | 42.5 |     22.5 |       82   |       70.6 |   nan   |
| ('SimGCD raso (K estimado)', 40)     | 57.7 |     17.7 |       81.9 |       73.4 |   nan   |
| ('SimGCD raso (K oráculo)', 0)       |  0   |      0   |       91.3 |      nan   |   nan   |
| ('SimGCD raso (K oráculo)', 5)       |  5   |      0   |       89.8 |       74   |   nan   |
| ('SimGCD raso (K oráculo)', 10)      | 10   |      0   |       88.5 |       79.6 |   nan   |
| ('SimGCD raso (K oráculo)', 20)      | 20   |      0   |       86   |       76.8 |   nan   |
| ('SimGCD raso (K oráculo)', 40)      | 40   |      0   |       83   |       75.2 |   nan   |
| ('dicotomia-euclid + ruído', 0)      | 13.4 |     13.4 |       77.6 |      nan   |   nan   |
| ('dicotomia-euclid + ruído', 5)      | 22.5 |     17.9 |       74.9 |       56.4 |    76.6 |
| ('dicotomia-euclid + ruído', 10)     | 32.8 |     22.8 |       73.6 |       65.4 |    77.9 |
| ('dicotomia-euclid + ruído', 20)     | 44.9 |     24.9 |       71.1 |       60.6 |    77.3 |
| ('dicotomia-euclid + ruído', 40)     | 53.1 |     15.7 |       65.2 |       54.2 |    75.6 |
| ('dicotomia-hgb + ruído', 0)         | 14.2 |     14.2 |       82.2 |      nan   |   nan   |
| ('dicotomia-hgb + ruído', 5)         | 17   |     12   |       80.6 |       73.2 |    86.4 |
| ('dicotomia-hgb + ruído', 10)        | 23.8 |     13.8 |       80.5 |       76.2 |    88.7 |
| ('dicotomia-hgb + ruído', 20)        | 26.9 |      7.5 |       75.5 |       65.5 |    87.7 |
| ('dicotomia-hgb + ruído', 40)        | 49.6 |     10.8 |       71.5 |       60.2 |    87.7 |
| ('dicotomia-hgb corrigida', 0)       |  8.6 |      8.6 |       82.5 |      nan   |   nan   |
| ('dicotomia-hgb corrigida', 5)       | 12.6 |      8   |       80.3 |       69.2 |   nan   |
| ('dicotomia-hgb corrigida', 10)      | 18.1 |      8.1 |       80   |       72   |   nan   |
| ('dicotomia-hgb corrigida', 20)      | 21.8 |      4.6 |       74.6 |       62.5 |   nan   |
| ('dicotomia-hgb corrigida', 40)      | 44.5 |      7.9 |       70.8 |       59.1 |   nan   |


Ours minus other (paired by scenario and seed):

|   K | vs                       | metric   |   ours_minus_other |   n |        p |
|----:|:-------------------------|:---------|-------------------:|----:|---------:|
|   0 | SS-kmeans (K estimado)   | k_err    |            -10.2   |  10 | 0.1074   |
|   0 | SS-kmeans (K estimado)   | test_all |             -0.03  |  10 | 0.001953 |
|   0 | dicotomia-euclid + ruído | k_err    |              0.8   |  10 | 0.9023   |
|   0 | dicotomia-euclid + ruído | test_all |              0.046 |  10 | 0.001953 |
|   5 | SS-kmeans (K estimado)   | k_err    |            -15.5   |  10 | 0.009766 |
|   5 | SS-kmeans (K estimado)   | test_all |              0.009 |  10 | 0.3359   |
|   5 | dicotomia-euclid + ruído | k_err    |             -5.9   |  10 | 0.1602   |
|   5 | dicotomia-euclid + ruído | test_all |              0.057 |  10 | 0.001953 |
|  10 | SS-kmeans (K estimado)   | k_err    |            -13.6   |  10 | 0.009766 |
|  10 | SS-kmeans (K estimado)   | test_all |              0.024 |  10 | 0.01172  |
|  10 | dicotomia-euclid + ruído | k_err    |             -9     |  10 | 0.08398  |
|  10 | dicotomia-euclid + ruído | test_all |              0.068 |  10 | 0.001953 |
|  20 | SS-kmeans (K estimado)   | k_err    |            -15     |  10 | 0.009766 |
|  20 | SS-kmeans (K estimado)   | test_all |              0.013 |  10 | 0.1836   |
|  20 | dicotomia-euclid + ruído | k_err    |            -17.4   |  10 | 0.005859 |
|  20 | dicotomia-euclid + ruído | test_all |              0.044 |  10 | 0.001953 |
|  40 | SS-kmeans (K estimado)   | k_err    |             -8.9   |  10 | 0.168    |
|  40 | SS-kmeans (K estimado)   | test_all |              0.044 |  10 | 0.009766 |
|  40 | dicotomia-euclid + ruído | k_err    |             -4.9   |  10 | 0.3125   |
|  40 | dicotomia-euclid + ruído | test_all |              0.063 |  10 | 0.003906 |



## Omniglot · HOG

|                                      |   K̂ |   |K̂−K| |   test all |   test new |   AUROC |
|:-------------------------------------|-----:|---------:|-----------:|-----------:|--------:|
| ('SS-kmeans (K estimado)', 0)        | 38   |     38   |       67.5 |      nan   |   nan   |
| ('SS-kmeans (K estimado)', 5)        | 47.6 |     42.6 |       65.8 |       44   |   nan   |
| ('SS-kmeans (K estimado)', 10)       | 45.4 |     35.4 |       63.3 |       50.8 |   nan   |
| ('SS-kmeans (K estimado)', 20)       | 50.8 |     34.6 |       58.8 |       45.2 |   nan   |
| ('SS-kmeans (K estimado)', 40)       | 62.5 |     23.1 |       53   |       41   |   nan   |
| ('SimGCD raso (K da dicotomia)', 0)  | 24.2 |     24.2 |       73.3 |      nan   |   nan   |
| ('SimGCD raso (K da dicotomia)', 5)  | 35.4 |     30.4 |       71.8 |       53.2 |   nan   |
| ('SimGCD raso (K da dicotomia)', 10) | 43.3 |     33.3 |       70   |       57.8 |   nan   |
| ('SimGCD raso (K da dicotomia)', 20) | 36.9 |     18.1 |       70.2 |       57   |   nan   |
| ('SimGCD raso (K da dicotomia)', 40) | 87   |     47   |       65.4 |       53.1 |   nan   |
| ('SimGCD raso (K estimado)', 0)      | 38   |     38   |       70.5 |      nan   |   nan   |
| ('SimGCD raso (K estimado)', 5)      | 47.6 |     42.6 |       69.4 |       48.8 |   nan   |
| ('SimGCD raso (K estimado)', 10)     | 45.4 |     35.4 |       70   |       55.6 |   nan   |
| ('SimGCD raso (K estimado)', 20)     | 50.8 |     34.6 |       67.6 |       51.5 |   nan   |
| ('SimGCD raso (K estimado)', 40)     | 62.5 |     23.1 |       66.4 |       53.4 |   nan   |
| ('SimGCD raso (K oráculo)', 0)       |  0   |      0   |       80.6 |      nan   |   nan   |
| ('SimGCD raso (K oráculo)', 5)       |  5   |      0   |       78.1 |       64.4 |   nan   |
| ('SimGCD raso (K oráculo)', 10)      | 10   |      0   |       74.7 |       59.2 |   nan   |
| ('SimGCD raso (K oráculo)', 20)      | 20   |      0   |       71.6 |       58.9 |   nan   |
| ('SimGCD raso (K oráculo)', 40)      | 40   |      0   |       67.7 |       55.6 |   nan   |
| ('dicotomia-euclid + ruído', 0)      | 13.6 |     13.6 |       69.7 |      nan   |   nan   |
| ('dicotomia-euclid + ruído', 5)      | 26.8 |     23.8 |       66.5 |       38.4 |    65.2 |
| ('dicotomia-euclid + ruído', 10)     | 29.1 |     23.7 |       63.8 |       42.8 |    62.8 |
| ('dicotomia-euclid + ruído', 20)     | 20.9 |      7.7 |       59   |       39.6 |    62.8 |
| ('dicotomia-euclid + ruído', 40)     | 59.3 |     32.5 |       53.9 |       38.4 |    61.9 |
| ('dicotomia-hgb + ruído', 0)         | 24.2 |     24.2 |       70   |      nan   |   nan   |
| ('dicotomia-hgb + ruído', 5)         | 35.4 |     30.4 |       66.8 |       57.2 |    82.3 |
| ('dicotomia-hgb + ruído', 10)        | 43.3 |     33.3 |       66.2 |       56.8 |    79.9 |
| ('dicotomia-hgb + ruído', 20)        | 36.9 |     18.1 |       60.9 |       49.2 |    80.3 |
| ('dicotomia-hgb + ruído', 40)        | 87   |     47   |       58.1 |       48.1 |    78.8 |
| ('dicotomia-hgb corrigida', 0)       |  7.8 |      7.8 |       70.2 |      nan   |   nan   |
| ('dicotomia-hgb corrigida', 5)       | 14   |     12   |       66.2 |       42   |   nan   |
| ('dicotomia-hgb corrigida', 10)      | 14.1 |      7.5 |       63.9 |       41.2 |   nan   |
| ('dicotomia-hgb corrigida', 20)      | 15.3 |      9.3 |       58   |       37.4 |   nan   |
| ('dicotomia-hgb corrigida', 40)      | 56   |     19.2 |       55.8 |       42.7 |   nan   |


Ours minus other (paired by scenario and seed):

|   K | vs                       | metric   |   ours_minus_other |   n |        p |
|----:|:-------------------------|:---------|-------------------:|----:|---------:|
|   0 | SS-kmeans (K estimado)   | k_err    |            -13.8   |  10 | 0.07031  |
|   0 | SS-kmeans (K estimado)   | test_all |              0.025 |  10 | 0.007812 |
|   0 | dicotomia-euclid + ruído | k_err    |             10.6   |  10 | 0.1074   |
|   0 | dicotomia-euclid + ruído | test_all |              0.003 |  10 | 0.9219   |
|   5 | SS-kmeans (K estimado)   | k_err    |            -12.2   |  10 | 0.1934   |
|   5 | SS-kmeans (K estimado)   | test_all |              0.011 |  10 | 0.08984  |
|   5 | dicotomia-euclid + ruído | k_err    |              6.6   |  10 | 0.334    |
|   5 | dicotomia-euclid + ruído | test_all |              0.003 |  10 | 0.625    |
|  10 | SS-kmeans (K estimado)   | k_err    |             -2.1   |  10 | 0.8242   |
|  10 | SS-kmeans (K estimado)   | test_all |              0.028 |  10 | 0.009766 |
|  10 | dicotomia-euclid + ruído | k_err    |              9.6   |  10 | 0.2637   |
|  10 | dicotomia-euclid + ruído | test_all |              0.024 |  10 | 0.01367  |
|  20 | SS-kmeans (K estimado)   | k_err    |            -16.5   |  10 | 0.04297  |
|  20 | SS-kmeans (K estimado)   | test_all |              0.021 |  10 | 0.02734  |
|  20 | dicotomia-euclid + ruído | k_err    |             10.4   |  10 | 0.03906  |
|  20 | dicotomia-euclid + ruído | test_all |              0.02  |  10 | 0.123    |
|  40 | SS-kmeans (K estimado)   | k_err    |             23.9   |  10 | 0.0625   |
|  40 | SS-kmeans (K estimado)   | test_all |              0.051 |  10 | 0.001953 |
|  40 | dicotomia-euclid + ruído | k_err    |             14.5   |  10 | 0.1562   |
|  40 | dicotomia-euclid + ruído | test_all |              0.041 |  10 | 0.08398  |



## CUB · DINOv2

|                                      |   K̂ |   |K̂−K| |   test all |   test new |   AUROC |
|:-------------------------------------|-----:|---------:|-----------:|-----------:|--------:|
| ('SS-kmeans (K estimado)', 0)        | 13.6 |     13.6 |       89.1 |      nan   |   nan   |
| ('SS-kmeans (K estimado)', 5)        | 11.9 |      6.9 |       86.1 |       81.2 |   nan   |
| ('SS-kmeans (K estimado)', 10)       | 20.7 |     12.7 |       83.1 |       77.6 |   nan   |
| ('SS-kmeans (K estimado)', 20)       | 27.8 |     12.6 |       78.6 |       72   |   nan   |
| ('SS-kmeans (K estimado)', 30)       | 33.1 |      9.9 |       74.6 |       71.1 |   nan   |
| ('SimGCD raso (K da dicotomia)', 0)  |  6.4 |      6.4 |       90.1 |      nan   |   nan   |
| ('SimGCD raso (K da dicotomia)', 5)  |  7.8 |      3.6 |       89.7 |       76.8 |   nan   |
| ('SimGCD raso (K da dicotomia)', 10) | 14.4 |      5.4 |       87.4 |       76.6 |   nan   |
| ('SimGCD raso (K da dicotomia)', 20) | 19.3 |      6.1 |       84.6 |       72.7 |   nan   |
| ('SimGCD raso (K da dicotomia)', 30) | 26.1 |      6.9 |       82.5 |       74.3 |   nan   |
| ('SimGCD raso (K estimado)', 0)      | 10.2 |     10.2 |       88.2 |      nan   |   nan   |
| ('SimGCD raso (K estimado)', 5)      | 11.9 |      6.9 |       89.3 |       78.8 |   nan   |
| ('SimGCD raso (K estimado)', 10)     | 16.5 |      9.1 |       86.4 |       73.4 |   nan   |
| ('SimGCD raso (K estimado)', 20)     | 27.8 |     12.6 |       84.1 |       72.7 |   nan   |
| ('SimGCD raso (K estimado)', 30)     | 35.7 |     10.7 |       82   |       73.2 |   nan   |
| ('SimGCD raso (K oráculo)', 0)       |  0   |      0   |       91.4 |      nan   |   nan   |
| ('SimGCD raso (K oráculo)', 5)       |  5   |      0   |       90.2 |       82   |   nan   |
| ('SimGCD raso (K oráculo)', 10)      | 10   |      0   |       88.8 |       80.8 |   nan   |
| ('SimGCD raso (K oráculo)', 20)      | 20   |      0   |       86.2 |       75.3 |   nan   |
| ('SimGCD raso (K oráculo)', 30)      | 30   |      0   |       83.9 |       75.1 |   nan   |
| ('dicotomia-euclid + ruído', 0)      |  6.2 |      6.2 |       88.3 |      nan   |   nan   |
| ('dicotomia-euclid + ruído', 5)      | 10.4 |      5.4 |       86.9 |       78.8 |    84.4 |
| ('dicotomia-euclid + ruído', 10)     | 13.8 |      4.8 |       85.2 |       78.4 |    80.3 |
| ('dicotomia-euclid + ruído', 20)     | 26.1 |      9.1 |       83   |       77.6 |    80.5 |
| ('dicotomia-euclid + ruído', 30)     | 28.6 |      7.4 |       79   |       72.1 |    81.2 |
| ('dicotomia-hgb + ruído', 0)         |  6.4 |      6.4 |       88.3 |      nan   |   nan   |
| ('dicotomia-hgb + ruído', 5)         |  7.8 |      3.6 |       86.8 |       78.8 |    85.2 |
| ('dicotomia-hgb + ruído', 10)        | 14.4 |      5.4 |       84.3 |       74.4 |    81.7 |
| ('dicotomia-hgb + ruído', 20)        | 19.3 |      6.1 |       80.2 |       71.8 |    82.5 |
| ('dicotomia-hgb + ruído', 30)        | 26.1 |      6.9 |       76.8 |       69.8 |    82.6 |
| ('dicotomia-hgb corrigida', 0)       |  4   |      4   |       88.4 |      nan   |   nan   |
| ('dicotomia-hgb corrigida', 5)       |  6.9 |      3.7 |       86.4 |       73.2 |   nan   |
| ('dicotomia-hgb corrigida', 10)      | 11.8 |      4.6 |       84.1 |       72.8 |   nan   |
| ('dicotomia-hgb corrigida', 20)      | 16.6 |      6.2 |       79.3 |       70.7 |   nan   |
| ('dicotomia-hgb corrigida', 30)      | 24.2 |      7.8 |       76.5 |       69.4 |   nan   |


Ours minus other (paired by scenario and seed):

|   K | vs                       | metric   |   ours_minus_other |   n |        p |
|----:|:-------------------------|:---------|-------------------:|----:|---------:|
|   0 | SS-kmeans (K estimado)   | k_err    |             -7.2   |  10 | 0.001953 |
|   0 | SS-kmeans (K estimado)   | test_all |             -0.009 |  10 | 0.1074   |
|   0 | dicotomia-euclid + ruído | k_err    |              0.2   |  10 | 0.9219   |
|   0 | dicotomia-euclid + ruído | test_all |             -0     |  10 | 0.9219   |
|   5 | SS-kmeans (K estimado)   | k_err    |             -3.3   |  10 | 0.1289   |
|   5 | SS-kmeans (K estimado)   | test_all |              0.007 |  10 | 0.1562   |
|   5 | dicotomia-euclid + ruído | k_err    |             -1.8   |  10 | 0.4141   |
|   5 | dicotomia-euclid + ruído | test_all |             -0.001 |  10 | 0.8379   |
|  10 | SS-kmeans (K estimado)   | k_err    |             -7.3   |  10 | 0.04297  |
|  10 | SS-kmeans (K estimado)   | test_all |              0.013 |  10 | 0.3125   |
|  10 | dicotomia-euclid + ruído | k_err    |              0.6   |  10 | 0.6602   |
|  10 | dicotomia-euclid + ruído | test_all |             -0.009 |  10 | 0.1953   |
|  20 | SS-kmeans (K estimado)   | k_err    |             -6.5   |  10 | 0.02344  |
|  20 | SS-kmeans (K estimado)   | test_all |              0.016 |  10 | 0.01953  |
|  20 | dicotomia-euclid + ruído | k_err    |             -3     |  10 | 1        |
|  20 | dicotomia-euclid + ruído | test_all |             -0.029 |  10 | 0.003906 |
|  30 | SS-kmeans (K estimado)   | k_err    |             -3     |  10 | 0.418    |
|  30 | SS-kmeans (K estimado)   | test_all |              0.021 |  10 | 0.04297  |
|  30 | dicotomia-euclid + ruído | k_err    |             -0.5   |  10 | 0.8125   |
|  30 | dicotomia-euclid + ruído | test_all |             -0.022 |  10 | 0.06055  |



## ShapesAll · MiniRocket

|                                      |   K̂ |   |K̂−K| |   test all |   test new |   AUROC |
|:-------------------------------------|-----:|---------:|-----------:|-----------:|--------:|
| ('SS-kmeans (K estimado)', 0)        |  6.2 |      6.2 |       87.5 |      nan   |   nan   |
| ('SS-kmeans (K estimado)', 5)        | 17.2 |     12.6 |       80.3 |       68.8 |   nan   |
| ('SS-kmeans (K estimado)', 10)       | 15.4 |      6.6 |       76.2 |       66.4 |   nan   |
| ('SS-kmeans (K estimado)', 15)       | 20.6 |      6   |       72   |       62.7 |   nan   |
| ('SS-kmeans (K estimado)', 20)       | 22.6 |      3.4 |       70.3 |       63.8 |   nan   |
| ('SimGCD raso (K da dicotomia)', 0)  |  7.8 |      7.8 |       88.7 |      nan   |   nan   |
| ('SimGCD raso (K da dicotomia)', 5)  | 14.2 |      9.2 |       86.5 |       73.6 |   nan   |
| ('SimGCD raso (K da dicotomia)', 10) | 15.4 |      5.4 |       86.6 |       77.2 |   nan   |
| ('SimGCD raso (K da dicotomia)', 15) | 24   |      9   |       83.9 |       73.3 |   nan   |
| ('SimGCD raso (K da dicotomia)', 20) | 30   |     10   |       82.5 |       74.6 |   nan   |
| ('SimGCD raso (K estimado)', 0)      |  6.2 |      6.2 |       89.5 |      nan   |   nan   |
| ('SimGCD raso (K estimado)', 5)      |  8.6 |      6.8 |       84.8 |       62.4 |   nan   |
| ('SimGCD raso (K estimado)', 10)     | 17.6 |      8.4 |       83.4 |       70   |   nan   |
| ('SimGCD raso (K estimado)', 15)     | 20.6 |      6   |       83.7 |       73.1 |   nan   |
| ('SimGCD raso (K estimado)', 20)     | 22.6 |      3.4 |       83.3 |       75.4 |   nan   |
| ('SimGCD raso (K oráculo)', 0)       |  0   |      0   |       92.7 |      nan   |   nan   |
| ('SimGCD raso (K oráculo)', 5)       |  5   |      0   |       90.9 |       83.2 |   nan   |
| ('SimGCD raso (K oráculo)', 10)      | 10   |      0   |       88.2 |       78   |   nan   |
| ('SimGCD raso (K oráculo)', 15)      | 15   |      0   |       85.7 |       76   |   nan   |
| ('SimGCD raso (K oráculo)', 20)      | 20   |      0   |       83.4 |       75.2 |   nan   |
| ('dicotomia-euclid + ruído', 0)      | 11   |     11   |       84.5 |      nan   |   nan   |
| ('dicotomia-euclid + ruído', 5)      | 15.6 |     10.6 |       82.3 |       68   |    86.5 |
| ('dicotomia-euclid + ruído', 10)     | 20.8 |     10.8 |       77.6 |       70   |    85.3 |
| ('dicotomia-euclid + ruído', 15)     | 22.2 |      7.2 |       73.1 |       59.7 |    82.9 |
| ('dicotomia-euclid + ruído', 20)     | 31.4 |     13.4 |       70.2 |       60.6 |    83.8 |
| ('dicotomia-hgb + ruído', 0)         |  7.8 |      7.8 |       88.8 |      nan   |   nan   |
| ('dicotomia-hgb + ruído', 5)         | 14.2 |      9.2 |       85.5 |       70.4 |    92.2 |
| ('dicotomia-hgb + ruído', 10)        | 15.4 |      5.4 |       84.2 |       77.6 |    92.9 |
| ('dicotomia-hgb + ruído', 15)        | 24   |      9   |       82.1 |       69.1 |    92   |
| ('dicotomia-hgb + ruído', 20)        | 30   |     10   |       79.4 |       70.8 |    91.6 |
| ('dicotomia-hgb corrigida', 0)       |  4   |      4   |       89.5 |      nan   |   nan   |
| ('dicotomia-hgb corrigida', 5)       |  8.8 |      4.2 |       84.6 |       68.8 |   nan   |
| ('dicotomia-hgb corrigida', 10)      | 14   |      4.4 |       84.1 |       76.4 |   nan   |
| ('dicotomia-hgb corrigida', 15)      | 22.8 |      7.8 |       81.6 |       69.3 |   nan   |
| ('dicotomia-hgb corrigida', 20)      | 28.6 |      8.6 |       78.8 |       71   |   nan   |


Ours minus other (paired by scenario and seed):

|   K | vs                       | metric   |   ours_minus_other |   n |   p |
|----:|:-------------------------|:---------|-------------------:|----:|----:|
|   0 | SS-kmeans (K estimado)   | k_err    |              1.6   |   5 | nan |
|   0 | SS-kmeans (K estimado)   | test_all |              0.013 |   5 | nan |
|   0 | dicotomia-euclid + ruído | k_err    |             -3.2   |   5 | nan |
|   0 | dicotomia-euclid + ruído | test_all |              0.043 |   5 | nan |
|   5 | SS-kmeans (K estimado)   | k_err    |             -3.4   |   5 | nan |
|   5 | SS-kmeans (K estimado)   | test_all |              0.052 |   5 | nan |
|   5 | dicotomia-euclid + ruído | k_err    |             -1.4   |   5 | nan |
|   5 | dicotomia-euclid + ruído | test_all |              0.032 |   5 | nan |
|  10 | SS-kmeans (K estimado)   | k_err    |             -1.2   |   5 | nan |
|  10 | SS-kmeans (K estimado)   | test_all |              0.08  |   5 | nan |
|  10 | dicotomia-euclid + ruído | k_err    |             -5.4   |   5 | nan |
|  10 | dicotomia-euclid + ruído | test_all |              0.066 |   5 | nan |
|  15 | SS-kmeans (K estimado)   | k_err    |              3     |   5 | nan |
|  15 | SS-kmeans (K estimado)   | test_all |              0.101 |   5 | nan |
|  15 | dicotomia-euclid + ruído | k_err    |              1.8   |   5 | nan |
|  15 | dicotomia-euclid + ruído | test_all |              0.089 |   5 | nan |
|  20 | SS-kmeans (K estimado)   | k_err    |              6.6   |   5 | nan |
|  20 | SS-kmeans (K estimado)   | test_all |              0.091 |   5 | nan |
|  20 | dicotomia-euclid + ruído | k_err    |             -3.4   |   5 | nan |
|  20 | dicotomia-euclid + ruído | test_all |              0.092 |   5 | nan |

