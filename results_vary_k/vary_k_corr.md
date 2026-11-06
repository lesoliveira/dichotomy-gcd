# Bias correction of K̂

Offset rate: mean K̂₀ 9.8 vs true known-dominated clusters 12.9, r = 0.76

Offset pseudo: mean K̂₀ 2.6 vs true known-dominated clusters 12.9, r = 0.74

Offset binom: mean K̂₀ 22.6 vs true known-dominated clusters 12.9, r = 0.82


## Per setting, K > 0

|                                                              |   K̂−K |   |K̂−K| |   test all % |
|:-------------------------------------------------------------|-------:|---------:|-------------:|
| ('cub_dinov2', 'SS-kmeans (K estimado)')                     |    7.1 |     10.5 |         80.6 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia)')               |    0.6 |      5.5 |         86.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [binom]')       |  -10.9 |     11   |         81.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [pseudo]')      |    0.6 |      5.4 |         86.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [rate]')        |   -1.4 |      5.6 |         85.7 |
| ('cub_dinov2', 'SimGCD raso (K estimado)')                   |    6.7 |      9.8 |         85.4 |
| ('cub_dinov2', 'SimGCD raso (K oráculo)')                    |    0   |      0   |         87.3 |
| ('cub_dinov2', 'dicotomia-euclid [binom]')                   |  -11.4 |     11.5 |         78.5 |
| ('cub_dinov2', 'dicotomia-euclid [none]')                    |    3.5 |      6.7 |         83.5 |
| ('cub_dinov2', 'dicotomia-euclid [pseudo]')                  |    2.6 |      5.8 |         83.6 |
| ('cub_dinov2', 'dicotomia-euclid [rate]')                    |    0.5 |      5   |         83.3 |
| ('cub_dinov2', 'dicotomia-hgb [binom]')                      |  -10.9 |     11   |         77.9 |
| ('cub_dinov2', 'dicotomia-hgb [none]')                       |    0.6 |      5.5 |         82   |
| ('cub_dinov2', 'dicotomia-hgb [pseudo]')                     |    0.6 |      5.4 |         82   |
| ('cub_dinov2', 'dicotomia-hgb [rate]')                       |   -1.4 |      5.6 |         81.6 |
| ('omniglot_dinov2', 'SS-kmeans (K estimado)')                |   23.2 |     24.3 |         74.8 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia)')          |   10.6 |     11   |         85.1 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [binom]')  |   -7.2 |      9.2 |         82.1 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [pseudo]') |    9.2 |      9.7 |         85.3 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [rate]')   |    5.5 |      7.2 |         85.8 |
| ('omniglot_dinov2', 'SimGCD raso (K estimado)')              |   17.8 |     18.3 |         83.6 |
| ('omniglot_dinov2', 'SimGCD raso (K oráculo)')               |    0   |      0   |         86.8 |
| ('omniglot_dinov2', 'dicotomia-euclid [binom]')              |  -11.6 |     11.7 |         66.3 |
| ('omniglot_dinov2', 'dicotomia-euclid [none]')               |   19.6 |     20.3 |         71.2 |
| ('omniglot_dinov2', 'dicotomia-euclid [pseudo]')             |   16   |     16.7 |         71.1 |
| ('omniglot_dinov2', 'dicotomia-euclid [rate]')               |    8   |     11.2 |         70.5 |
| ('omniglot_dinov2', 'dicotomia-hgb [binom]')                 |   -7.2 |      9.2 |         72.5 |
| ('omniglot_dinov2', 'dicotomia-hgb [none]')                  |   10.6 |     11   |         77   |
| ('omniglot_dinov2', 'dicotomia-hgb [pseudo]')                |    9.2 |      9.7 |         76.9 |
| ('omniglot_dinov2', 'dicotomia-hgb [rate]')                  |    5.5 |      7.2 |         76.4 |
| ('omniglot_hog', 'SS-kmeans (K estimado)')                   |   32.8 |     33.9 |         60.2 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia)')             |   31.9 |     32.2 |         69.3 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [binom]')     |   -7.4 |     11   |         68.9 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [pseudo]')    |   19.8 |     20.4 |         71.1 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [rate]')      |    6.1 |     12   |         71.1 |
| ('omniglot_hog', 'SimGCD raso (K estimado)')                 |   32.8 |     33.9 |         68.4 |
| ('omniglot_hog', 'SimGCD raso (K oráculo)')                  |    0   |      0   |         73   |
| ('omniglot_hog', 'dicotomia-euclid [binom]')                 |  -12.3 |     13.2 |         57.6 |
| ('omniglot_hog', 'dicotomia-euclid [none]')                  |   15.3 |     21.9 |         60.8 |
| ('omniglot_hog', 'dicotomia-euclid [pseudo]')                |   10.7 |     17.9 |         60.7 |
| ('omniglot_hog', 'dicotomia-euclid [rate]')                  |   -1.1 |     10.4 |         59.6 |
| ('omniglot_hog', 'dicotomia-hgb [binom]')                    |   -7.4 |     11   |         58.8 |
| ('omniglot_hog', 'dicotomia-hgb [none]')                     |   31.9 |     32.2 |         63   |
| ('omniglot_hog', 'dicotomia-hgb [pseudo]')                   |   19.8 |     20.4 |         62.5 |
| ('omniglot_hog', 'dicotomia-hgb [rate]')                     |    6.1 |     12   |         61   |
| ('ts_ShapesAll', 'SS-kmeans (K estimado)')                   |    6.4 |      7.2 |         74.7 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia)')             |    8.4 |      8.4 |         84.9 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [binom]')     |    0.2 |      4.2 |         85.1 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [pseudo]')    |    6   |      6.2 |         85.4 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [rate]')      |    6   |      6.2 |         85.8 |
| ('ts_ShapesAll', 'SimGCD raso (K estimado)')                 |    4.8 |      6.2 |         83.8 |
| ('ts_ShapesAll', 'SimGCD raso (K oráculo)')                  |    0   |      0   |         87.1 |
| ('ts_ShapesAll', 'dicotomia-euclid [binom]')                 |   -2.2 |      4.6 |         70.2 |
| ('ts_ShapesAll', 'dicotomia-euclid [none]')                  |   10   |     10.5 |         75.8 |
| ('ts_ShapesAll', 'dicotomia-euclid [pseudo]')                |    7.5 |      8   |         74.4 |
| ('ts_ShapesAll', 'dicotomia-euclid [rate]')                  |    5.3 |      6.6 |         73.5 |
| ('ts_ShapesAll', 'dicotomia-hgb [binom]')                    |    0.2 |      4.2 |         78.6 |
| ('ts_ShapesAll', 'dicotomia-hgb [none]')                     |    8.4 |      8.4 |         82.8 |
| ('ts_ShapesAll', 'dicotomia-hgb [pseudo]')                   |    6   |      6.2 |         82.2 |
| ('ts_ShapesAll', 'dicotomia-hgb [rate]')                     |    6   |      6.2 |         82.3 |



## Pooled, K > 0

| name                                  |   K̂−K |   |K̂−K| |   test all % |
|:--------------------------------------|-------:|---------:|-------------:|
| SS-kmeans (K estimado)                |   19   |     20.7 |         72.3 |
| SimGCD raso (K da dicotomia)          |   13.5 |     15.1 |         80.8 |
| SimGCD raso (K da dicotomia) [binom]  |   -7.3 |      9.5 |         78.5 |
| SimGCD raso (K da dicotomia) [pseudo] |    9.3 |     11   |         81.5 |
| SimGCD raso (K da dicotomia) [rate]   |    3.8 |      8   |         81.6 |
| SimGCD raso (K estimado)              |   17.1 |     18.6 |         79.8 |
| SimGCD raso (K oráculo)               |    0   |      0   |         83   |
| dicotomia-euclid [binom]              |  -10.4 |     11   |         67.9 |
| dicotomia-euclid [none]               |   12.4 |     15.5 |         72.4 |
| dicotomia-euclid [pseudo]             |    9.4 |     12.7 |         72.1 |
| dicotomia-euclid [rate]               |    2.8 |      8.5 |         71.5 |
| dicotomia-hgb [binom]                 |   -7.3 |      9.5 |         71   |
| dicotomia-hgb [none]                  |   13.5 |     15.1 |         75.3 |
| dicotomia-hgb [pseudo]                |    9.3 |     11   |         75   |
| dicotomia-hgb [rate]                  |    3.8 |      8   |         74.3 |



## Per setting, K = 0

|                                                              |   K̂−K |   |K̂−K| |   test all % |
|:-------------------------------------------------------------|-------:|---------:|-------------:|
| ('cub_dinov2', 'SS-kmeans (K estimado)')                     |   13.6 |     13.6 |         89.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia)')               |    6.4 |      6.4 |         90.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [binom]')       |    1   |      1   |         91.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [pseudo]')      |    5.8 |      5.8 |         90.1 |
| ('cub_dinov2', 'SimGCD raso (K da dicotomia) [rate]')        |    4   |      4   |         90.6 |
| ('cub_dinov2', 'SimGCD raso (K estimado)')                   |   10.2 |     10.2 |         88.2 |
| ('cub_dinov2', 'SimGCD raso (K oráculo)')                    |    0   |      0   |         91.4 |
| ('cub_dinov2', 'dicotomia-euclid [binom]')                   |    0   |      0   |         88.9 |
| ('cub_dinov2', 'dicotomia-euclid [none]')                    |    6.2 |      6.2 |         88.3 |
| ('cub_dinov2', 'dicotomia-euclid [pseudo]')                  |    5.4 |      5.4 |         88.3 |
| ('cub_dinov2', 'dicotomia-euclid [rate]')                    |    3.6 |      3.6 |         88.7 |
| ('cub_dinov2', 'dicotomia-hgb [binom]')                      |    1   |      1   |         88.5 |
| ('cub_dinov2', 'dicotomia-hgb [none]')                       |    6.4 |      6.4 |         88.3 |
| ('cub_dinov2', 'dicotomia-hgb [pseudo]')                     |    5.8 |      5.8 |         88.3 |
| ('cub_dinov2', 'dicotomia-hgb [rate]')                       |    4   |      4   |         88.4 |
| ('omniglot_dinov2', 'SS-kmeans (K estimado)')                |   24.4 |     24.4 |         85.2 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia)')          |   14.2 |     14.2 |         86.8 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [binom]')  |    0   |      0   |         91.3 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [pseudo]') |   12.6 |     12.6 |         88.5 |
| ('omniglot_dinov2', 'SimGCD raso (K da dicotomia) [rate]')   |    8.6 |      8.6 |         88.5 |
| ('omniglot_dinov2', 'SimGCD raso (K estimado)')              |   16.6 |     16.6 |         86.9 |
| ('omniglot_dinov2', 'SimGCD raso (K oráculo)')               |    0   |      0   |         91.3 |
| ('omniglot_dinov2', 'dicotomia-euclid [binom]')              |    0   |      0   |         78.5 |
| ('omniglot_dinov2', 'dicotomia-euclid [none]')               |   13.4 |     13.4 |         77.6 |
| ('omniglot_dinov2', 'dicotomia-euclid [pseudo]')             |   12.6 |     12.6 |         77.6 |
| ('omniglot_dinov2', 'dicotomia-euclid [rate]')               |    4.4 |      4.4 |         78.1 |
| ('omniglot_dinov2', 'dicotomia-hgb [binom]')                 |    0   |      0   |         82.9 |
| ('omniglot_dinov2', 'dicotomia-hgb [none]')                  |   14.2 |     14.2 |         82.2 |
| ('omniglot_dinov2', 'dicotomia-hgb [pseudo]')                |   12.6 |     12.6 |         82.2 |
| ('omniglot_dinov2', 'dicotomia-hgb [rate]')                  |    8.6 |      8.6 |         82.5 |
| ('omniglot_hog', 'SS-kmeans (K estimado)')                   |   38   |     38   |         67.5 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia)')             |   24.2 |     24.2 |         73.3 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [binom]')     |    0   |      0   |         80.6 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [pseudo]')    |   15.8 |     15.8 |         76.1 |
| ('omniglot_hog', 'SimGCD raso (K da dicotomia) [rate]')      |    7.8 |      7.8 |         77   |
| ('omniglot_hog', 'SimGCD raso (K estimado)')                 |   38   |     38   |         70.5 |
| ('omniglot_hog', 'SimGCD raso (K oráculo)')                  |    0   |      0   |         80.6 |
| ('omniglot_hog', 'dicotomia-euclid [binom]')                 |    0   |      0   |         70.1 |
| ('omniglot_hog', 'dicotomia-euclid [none]')                  |   13.6 |     13.6 |         69.7 |
| ('omniglot_hog', 'dicotomia-euclid [pseudo]')                |   11.4 |     11.4 |         69.9 |
| ('omniglot_hog', 'dicotomia-euclid [rate]')                  |    3.2 |      3.2 |         70.1 |
| ('omniglot_hog', 'dicotomia-hgb [binom]')                    |    0   |      0   |         70.1 |
| ('omniglot_hog', 'dicotomia-hgb [none]')                     |   24.2 |     24.2 |         70   |
| ('omniglot_hog', 'dicotomia-hgb [pseudo]')                   |   15.8 |     15.8 |         70.1 |
| ('omniglot_hog', 'dicotomia-hgb [rate]')                     |    7.8 |      7.8 |         70.2 |
| ('ts_ShapesAll', 'SS-kmeans (K estimado)')                   |    6.2 |      6.2 |         87.5 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia)')             |    7.8 |      7.8 |         88.7 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [binom]')     |    0.4 |      0.4 |         92.7 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [pseudo]')    |    4.4 |      4.4 |         89.8 |
| ('ts_ShapesAll', 'SimGCD raso (K da dicotomia) [rate]')      |    4   |      4   |         90.5 |
| ('ts_ShapesAll', 'SimGCD raso (K estimado)')                 |    6.2 |      6.2 |         89.5 |
| ('ts_ShapesAll', 'SimGCD raso (K oráculo)')                  |    0   |      0   |         92.7 |
| ('ts_ShapesAll', 'dicotomia-euclid [binom]')                 |    0.8 |      0.8 |         86.8 |
| ('ts_ShapesAll', 'dicotomia-euclid [none]')                  |   11   |     11   |         84.5 |
| ('ts_ShapesAll', 'dicotomia-euclid [pseudo]')                |    5   |      5   |         86   |
| ('ts_ShapesAll', 'dicotomia-euclid [rate]')                  |    5.8 |      5.8 |         86.3 |
| ('ts_ShapesAll', 'dicotomia-hgb [binom]')                    |    0.4 |      0.4 |         89.8 |
| ('ts_ShapesAll', 'dicotomia-hgb [none]')                     |    7.8 |      7.8 |         88.8 |
| ('ts_ShapesAll', 'dicotomia-hgb [pseudo]')                   |    4.4 |      4.4 |         89.5 |
| ('ts_ShapesAll', 'dicotomia-hgb [rate]')                     |    4   |      4   |         89.5 |



## Pooled, K = 0

| name                                  |   K̂−K |   |K̂−K| |   test all % |
|:--------------------------------------|-------:|---------:|-------------:|
| SS-kmeans (K estimado)                |   22.6 |     22.6 |         81.6 |
| SimGCD raso (K da dicotomia)          |   13.9 |     13.9 |         84.1 |
| SimGCD raso (K da dicotomia) [binom]  |    0.3 |      0.3 |         88.4 |
| SimGCD raso (K da dicotomia) [pseudo] |   10.4 |     10.4 |         85.6 |
| SimGCD raso (K da dicotomia) [rate]   |    6.4 |      6.4 |         86.1 |
| SimGCD raso (K estimado)              |   19.4 |     19.4 |         82.9 |
| SimGCD raso (K oráculo)               |    0   |      0   |         88.5 |
| dicotomia-euclid [binom]              |    0.1 |      0.1 |         80.3 |
| dicotomia-euclid [none]               |   11.1 |     11.1 |         79.4 |
| dicotomia-euclid [pseudo]             |    9.1 |      9.1 |         79.7 |
| dicotomia-euclid [rate]               |    4   |      4   |         80   |
| dicotomia-hgb [binom]                 |    0.3 |      0.3 |         81.8 |
| dicotomia-hgb [none]                  |   13.9 |     13.9 |         81.4 |
| dicotomia-hgb [pseudo]                |   10.4 |     10.4 |         81.5 |
| dicotomia-hgb [rate]                  |    6.4 |      6.4 |         81.7 |



## Paired tests, K > 0 (a vs b)

| a                                     | b                            | metric   |   mean_diff |   a_better |   b_better |   n |         p |
|:--------------------------------------|:-----------------------------|:---------|------------:|-----------:|-----------:|----:|----------:|
| dicotomia-hgb [rate]                  | dicotomia-hgb [none]         | err      |      -7.164 |         88 |         16 | 140 | 1.081e-12 |
| dicotomia-hgb [rate]                  | dicotomia-hgb [none]         | test_all |      -0.01  |         17 |         73 | 140 | 1.656e-12 |
| dicotomia-hgb [rate]                  | SS-kmeans (K estimado)       | err      |     -12.7   |        104 |         33 | 140 | 2.28e-13  |
| dicotomia-hgb [rate]                  | dicotomia-euclid [rate]      | err      |      -0.579 |         67 |         65 | 140 | 0.2756    |
| SimGCD raso (K da dicotomia) [rate]   | SimGCD raso (K da dicotomia) | test_all |       0.007 |         69 |         32 | 140 | 0.0001522 |
| SimGCD raso (K da dicotomia) [rate]   | SimGCD raso (K estimado)     | test_all |       0.018 |         94 |         40 | 140 | 1.108e-06 |
| dicotomia-hgb [pseudo]                | dicotomia-hgb [none]         | err      |      -4.086 |         65 |          2 | 140 | 2.148e-12 |
| dicotomia-hgb [pseudo]                | dicotomia-hgb [none]         | test_all |      -0.002 |          8 |         31 | 140 | 2.916e-05 |
| dicotomia-hgb [pseudo]                | SS-kmeans (K estimado)       | err      |      -9.621 |         98 |         37 | 140 | 2.774e-09 |
| dicotomia-hgb [pseudo]                | dicotomia-euclid [pseudo]    | err      |      -1.65  |         69 |         60 | 140 | 0.06904   |
| SimGCD raso (K da dicotomia) [pseudo] | SimGCD raso (K da dicotomia) | test_all |       0.006 |         47 |         17 | 140 | 8.176e-05 |
| SimGCD raso (K da dicotomia) [pseudo] | SimGCD raso (K estimado)     | test_all |       0.017 |         88 |         46 | 140 | 3.996e-06 |
| dicotomia-hgb [binom]                 | dicotomia-hgb [none]         | err      |      -5.621 |         77 |         59 | 140 | 0.006324  |
| dicotomia-hgb [binom]                 | dicotomia-hgb [none]         | test_all |      -0.043 |          6 |        132 | 140 | 1.597e-23 |
| dicotomia-hgb [binom]                 | SS-kmeans (K estimado)       | err      |     -11.16  |         92 |         44 | 140 | 1.069e-09 |
| dicotomia-hgb [binom]                 | dicotomia-euclid [binom]     | err      |      -1.536 |         62 |         33 | 140 | 0.006979  |
| SimGCD raso (K da dicotomia) [binom]  | SimGCD raso (K da dicotomia) | test_all |      -0.024 |         47 |         91 | 140 | 1.446e-05 |
| SimGCD raso (K da dicotomia) [binom]  | SimGCD raso (K estimado)     | test_all |      -0.013 |         48 |         86 | 140 | 0.006388  |



## By K (pooled over settings)

|   k_true |   ('K̂', 'SS-kmeans (K estimado)') |   ('K̂', 'SimGCD raso (K da dicotomia)') |   ('K̂', 'SimGCD raso (K da dicotomia) [binom]') |   ('K̂', 'SimGCD raso (K da dicotomia) [pseudo]') |   ('K̂', 'SimGCD raso (K da dicotomia) [rate]') |   ('K̂', 'SimGCD raso (K estimado)') |   ('K̂', 'SimGCD raso (K oráculo)') |   ('K̂', 'dicotomia-euclid [binom]') |   ('K̂', 'dicotomia-euclid [none]') |   ('K̂', 'dicotomia-euclid [pseudo]') |   ('K̂', 'dicotomia-euclid [rate]') |   ('K̂', 'dicotomia-hgb [binom]') |   ('K̂', 'dicotomia-hgb [none]') |   ('K̂', 'dicotomia-hgb [pseudo]') |   ('K̂', 'dicotomia-hgb [rate]') |   ('|K̂−K|', 'SS-kmeans (K estimado)') |   ('|K̂−K|', 'SimGCD raso (K da dicotomia)') |   ('|K̂−K|', 'SimGCD raso (K da dicotomia) [binom]') |   ('|K̂−K|', 'SimGCD raso (K da dicotomia) [pseudo]') |   ('|K̂−K|', 'SimGCD raso (K da dicotomia) [rate]') |   ('|K̂−K|', 'SimGCD raso (K estimado)') |   ('|K̂−K|', 'SimGCD raso (K oráculo)') |   ('|K̂−K|', 'dicotomia-euclid [binom]') |   ('|K̂−K|', 'dicotomia-euclid [none]') |   ('|K̂−K|', 'dicotomia-euclid [pseudo]') |   ('|K̂−K|', 'dicotomia-euclid [rate]') |   ('|K̂−K|', 'dicotomia-hgb [binom]') |   ('|K̂−K|', 'dicotomia-hgb [none]') |   ('|K̂−K|', 'dicotomia-hgb [pseudo]') |   ('|K̂−K|', 'dicotomia-hgb [rate]') |
|---------:|-----------------------------------:|-----------------------------------------:|-------------------------------------------------:|--------------------------------------------------:|------------------------------------------------:|-------------------------------------:|------------------------------------:|-------------------------------------:|------------------------------------:|--------------------------------------:|------------------------------------:|----------------------------------:|---------------------------------:|-----------------------------------:|---------------------------------:|---------------------------------------:|---------------------------------------------:|-----------------------------------------------------:|------------------------------------------------------:|----------------------------------------------------:|-----------------------------------------:|----------------------------------------:|-----------------------------------------:|----------------------------------------:|------------------------------------------:|----------------------------------------:|--------------------------------------:|-------------------------------------:|---------------------------------------:|-------------------------------------:|
|        5 |                               28.7 |                                     19.2 |                                              2.3 |                                              14.7 |                                            10.8 |                                 24.5 |                                   5 |                                  0.7 |                                19.3 |                                  16.5 |                                10.9 |                               2.3 |                             19.2 |                               14.7 |                             10.8 |                                   23.8 |                                         14.5 |                                                  4.5 |                                                  10   |                                                 7.4 |                                     20.1 |                                       0 |                                      4.8 |                                    15   |                                      12.1 |                                     6.8 |                                   4.5 |                                 14.5 |                                   10   |                                  7.4 |
|       10 |                               31.8 |                                     25.5 |                                              4.6 |                                              20   |                                            14.6 |                                 27.1 |                                  10 |                                  2.7 |                                24.6 |                                  20.4 |                                14.8 |                               4.6 |                             25.5 |                               20   |                             14.6 |                                   22.5 |                                         15.8 |                                                  7   |                                                  10.4 |                                                 6.4 |                                     18.3 |                                       0 |                                      7.6 |                                    16.2 |                                      12   |                                     6.8 |                                   7   |                                 15.8 |                                   10.4 |                                  6.4 |
|       15 |                               20.6 |                                     24   |                                             15.8 |                                              22.6 |                                            22.8 |                                 20.6 |                                  15 |                                 10   |                                22.2 |                                  21.4 |                                19.8 |                              15.8 |                             24   |                               22.6 |                             22.8 |                                    6   |                                          9   |                                                  3.6 |                                                   7.6 |                                                 7.8 |                                      6   |                                       0 |                                      5.4 |                                     7.2 |                                       6.4 |                                     4.8 |                                   3.6 |                                  9   |                                    7.6 |                                  7.8 |
|       20 |                               37.8 |                                     28   |                                              7.7 |                                              25.6 |                                            19.4 |                                 37.8 |                                  20 |                                  6.9 |                                30.7 |                                  27.7 |                                21.3 |                               7.7 |                             28   |                               25.6 |                             19.4 |                                   20.4 |                                         10.5 |                                                 13.4 |                                                   8.2 |                                                 7   |                                     20.4 |                                       0 |                                     14   |                                    13.8 |                                      11.3 |                                     8.9 |                                  13.4 |                                 10.5 |                                    8.2 |                                  7   |
|       30 |                               33.1 |                                     26.1 |                                             12.5 |                                              26.1 |                                            24.2 |                                 35.7 |                                  30 |                                 12.5 |                                28.6 |                                  28.6 |                                26   |                              12.5 |                             26.1 |                               26.1 |                             24.2 |                                    9.9 |                                          6.9 |                                                 17.5 |                                                   6.9 |                                                 7.8 |                                     10.7 |                                       0 |                                     17.5 |                                     7.4 |                                       7.4 |                                     7   |                                  17.5 |                                  6.9 |                                    6.9 |                                  7.8 |
|       40 |                               58.9 |                                     68.3 |                                             33.5 |                                              61.1 |                                            50.2 |                                 60.1 |                                  40 |                                 20.4 |                                56.2 |                                  53.4 |                                39.6 |                              33.5 |                             68.3 |                               61.1 |                             50.2 |                                   21.4 |                                         28.9 |                                                 13.4 |                                                  21.8 |                                                13.6 |                                     20.4 |                                       0 |                                     20.9 |                                    24.1 |                                      21.4 |                                    15.5 |                                  13.4 |                                 28.9 |                                   21.8 |                                 13.6 |

