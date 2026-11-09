# Baselines on full features (50 paired runs)

## Test accuracy, all classes (%)

| ds                            |   SS-kmeans (K estimado) [full] |   SS-kmeans (K oráculo) [full] |   SimGCD raso (K da dicotomia) [full] |   SimGCD raso (K da dicotomia) [pca64] |   SimGCD raso (K estimado) [best] |   SimGCD raso (K estimado) [full] |   SimGCD raso (K estimado) [pca64] |   SimGCD raso (K oráculo) [best] |   SimGCD raso (K oráculo) [full] |   SimGCD raso (K oráculo) [pca64] |
|:------------------------------|--------------------------------:|-------------------------------:|--------------------------------------:|---------------------------------------:|----------------------------------:|----------------------------------:|-----------------------------------:|---------------------------------:|---------------------------------:|----------------------------------:|
| cub_dinov2                    |                            78.1 |                           77.4 |                                  84.9 |                                   84.6 |                              84.9 |                              84.9 |                               84.1 |                             86.5 |                             86.5 |                              86.2 |
| omniglot_dinov2               |                            66.4 |                           64.9 |                                  86.8 |                                   85.2 |                              82.6 |                              82.6 |                               82   |                             88.2 |                             88.2 |                              86.3 |
| omniglot_hog                  |                            56.5 |                           55.6 |                                  64.6 |                                   70.2 |                              67.6 |                              60.7 |                               67.6 |                             71.6 |                             67.2 |                              71.6 |
| ts_Crop                       |                            47   |                           46.6 |                                  54.1 |                                   53   |                              53.2 |                              53.2 |                               48   |                             54.5 |                             54.5 |                              53   |
| ts_NonInvasiveFetalECGThorax1 |                            63.4 |                           64.5 |                                  79.5 |                                   83.5 |                              78.8 |                              75.3 |                               78.8 |                             85.2 |                             81.7 |                              85.2 |
| ts_ShapesAll                  |                            64.6 |                           65.2 |                                  79.2 |                                   82.5 |                              83.3 |                              78.5 |                               83.3 |                             84.1 |                             81.5 |                              84.1 |
| ts_SwedishLeaf                |                            66.2 |                           66.2 |                                  72.7 |                                   77.1 |                              72.7 |                              72.7 |                               72.7 |                             78.9 |                             74.2 |                              78.9 |


## Pooled

| name                                 |   test_all |   test_new |
|:-------------------------------------|-----------:|-----------:|
| SS-kmeans (K estimado) [full]        |      64.32 |      55.29 |
| SS-kmeans (K oráculo) [full]         |      63.84 |      54.65 |
| SimGCD raso (K da dicotomia) [full]  |      75.8  |      65.95 |
| SimGCD raso (K da dicotomia) [pca64] |      77.61 |      67.55 |
| SimGCD raso (K estimado) [best]      |      75.81 |      65.03 |
| SimGCD raso (K estimado) [full]      |      73.6  |      62.92 |
| SimGCD raso (K estimado) [pca64]     |      75.03 |      64.63 |
| SimGCD raso (K oráculo) [best]       |      79.54 |      70.26 |
| SimGCD raso (K oráculo) [full]       |      77.57 |      66.22 |
| SimGCD raso (K oráculo) [pca64]      |      78.93 |      69.43 |


## Paired tests (differences in points)

| a                                    | b                                    | metric   |   n |   diff_points |   a_wins |   b_wins |         p |
|:-------------------------------------|:-------------------------------------|:---------|----:|--------------:|---------:|---------:|----------:|
| SimGCD raso (K da dicotomia) [full]  | SimGCD raso (K estimado) [full]      | test_all |  50 |          2.2  |       31 |       15 | 0.001342  |
| SimGCD raso (K da dicotomia) [full]  | SimGCD raso (K estimado) [full]      | test_new |  50 |          3.04 |       29 |       15 | 0.007385  |
| SimGCD raso (K da dicotomia) [pca64] | SimGCD raso (K estimado) [best]      | test_all |  50 |          1.8  |       26 |       23 | 0.07744   |
| SimGCD raso (K da dicotomia) [full]  | SimGCD raso (K estimado) [best]      | test_all |  50 |         -0.01 |       24 |       24 | 0.8737    |
| SimGCD raso (K da dicotomia) [full]  | SimGCD raso (K oráculo) [full]       | test_all |  50 |         -1.77 |       11 |       31 | 6.972e-05 |
| SimGCD raso (K da dicotomia) [full]  | SimGCD raso (K da dicotomia) [pca64] | test_all |  50 |         -1.82 |       15 |       32 | 0.004876  |
| SimGCD raso (K estimado) [full]      | SimGCD raso (K estimado) [pca64]     | test_all |  50 |         -1.43 |       22 |       25 | 0.2597    |


## |K̂ − K|: search on full features vs. dichotomy (64-PCA)

| ds                            |   SimGCD raso (K da dicotomia) |   SimGCD raso (K estimado) |
|:------------------------------|-------------------------------:|---------------------------:|
| cub_dinov2                    |                            6.1 |                       11.2 |
| omniglot_dinov2               |                            7.5 |                       21.4 |
| omniglot_hog                  |                           18.1 |                       43.5 |
| ts_Crop                       |                            5.8 |                        3.2 |
| ts_NonInvasiveFetalECGThorax1 |                            3.6 |                        6.6 |
| ts_ShapesAll                  |                           10   |                        3.2 |
| ts_SwedishLeaf                |                            1   |                        1.6 |

