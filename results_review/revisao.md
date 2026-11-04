# Experimentos da revisão (sementes 20-24)

## 1. Proposto vs. SimGCD raso nas mesmas features fixas

| comparação                          | métrica   |   n |    dif | a_favor   |      p |
|:------------------------------------|:----------|----:|-------:|:----------|-------:|
| proposto − SimGCD raso (K estimado) | test_all  |  50 | -0.036 | 12/50     | 0      |
| proposto − SimGCD raso (K estimado) | test_new  |  50 | -0.024 | 19/50     | 0.0686 |
| proposto − SimGCD raso (K estimado) | all       |  50 | -0.033 | 14/50     | 0.0043 |
| proposto − SimGCD raso (K estimado) | new       |  50 | -0.039 | 15/50     | 0.0037 |
| proposto − SimGCD raso (K oráculo)  | test_all  |  50 | -0.075 | 3/50      | 0      |
| proposto − SimGCD raso (K oráculo)  | test_new  |  50 | -0.068 | 9/50      | 0      |
| proposto − SimGCD raso (K oráculo)  | all       |  50 | -0.117 | 1/50      | 0      |
| proposto − SimGCD raso (K oráculo)  | new       |  50 | -0.122 | 5/50      | 0      |

### Médias por conjunto

|                                          |   ('proposto', 'cub_dinov2') |   ('proposto', 'omniglot_dinov2') |   ('proposto', 'omniglot_hog') |   ('proposto', 'ts_Crop') |   ('proposto', 'ts_NonInvasiveFetalECGThorax1') |   ('proposto', 'ts_ShapesAll') |   ('proposto', 'ts_SwedishLeaf') |   ('valor', 'cub_dinov2') |   ('valor', 'omniglot_dinov2') |   ('valor', 'omniglot_hog') |   ('valor', 'ts_Crop') |   ('valor', 'ts_NonInvasiveFetalECGThorax1') |   ('valor', 'ts_ShapesAll') |   ('valor', 'ts_SwedishLeaf') |
|:-----------------------------------------|-----------------------------:|----------------------------------:|-------------------------------:|--------------------------:|------------------------------------------------:|-------------------------------:|---------------------------------:|--------------------------:|-------------------------------:|----------------------------:|-----------------------:|---------------------------------------------:|----------------------------:|------------------------------:|
| ('SimGCD raso (K estimado)', 'all')      |                        0.757 |                             0.705 |                          0.546 |                     0.413 |                                           0.746 |                          0.739 |                            0.717 |                     0.792 |                          0.736 |                       0.601 |                  0.443 |                                        0.761 |                       0.811 |                         0.69  |
| ('SimGCD raso (K estimado)', 'new')      |                        0.654 |                             0.615 |                          0.444 |                     0.393 |                                           0.713 |                          0.639 |                            0.672 |                     0.698 |                          0.661 |                       0.505 |                  0.445 |                                        0.724 |                       0.749 |                         0.589 |
| ('SimGCD raso (K estimado)', 'test_all') |                        0.802 |                             0.755 |                          0.609 |                     0.527 |                                           0.781 |                          0.794 |                            0.709 |                     0.841 |                          0.82  |                       0.676 |                  0.48  |                                        0.788 |                       0.833 |                         0.727 |
| ('SimGCD raso (K estimado)', 'test_new') |                        0.718 |                             0.655 |                          0.492 |                     0.49  |                                           0.723 |                          0.708 |                            0.608 |                     0.727 |                          0.706 |                       0.533 |                  0.5   |                                        0.729 |                       0.754 |                         0.584 |
| ('SimGCD raso (K oráculo)', 'all')       |                        0.757 |                             0.705 |                          0.546 |                     0.413 |                                           0.746 |                          0.739 |                            0.717 |                     0.849 |                          0.86  |                       0.715 |                  0.483 |                                        0.837 |                       0.825 |                         0.811 |
| ('SimGCD raso (K oráculo)', 'new')       |                        0.654 |                             0.615 |                          0.444 |                     0.393 |                                           0.713 |                          0.639 |                            0.672 |                     0.769 |                          0.793 |                       0.594 |                  0.472 |                                        0.807 |                       0.757 |                         0.72  |
| ('SimGCD raso (K oráculo)', 'test_all')  |                        0.802 |                             0.755 |                          0.609 |                     0.527 |                                           0.781 |                          0.794 |                            0.709 |                     0.862 |                          0.863 |                       0.716 |                  0.53  |                                        0.852 |                       0.841 |                         0.789 |
| ('SimGCD raso (K oráculo)', 'test_new')  |                        0.718 |                             0.655 |                          0.492 |                     0.49  |                                           0.723 |                          0.708 |                            0.608 |                     0.753 |                          0.775 |                       0.589 |                  0.515 |                                        0.786 |                       0.76  |                         0.648 |


## 2. Agrupamento a partir de P(mesma classe), mesmo K̂

### descoberta

| comparação                         | métrica   |   n |    dif | a_favor   |      p |
|:-----------------------------------|:----------|----:|-------:|:----------|-------:|
| espectral (P) − average linkage    | acc       |  50 | -0.049 | 16/50     | 0.0007 |
| Ward (espaço) − average linkage    | acc       |  50 | -0.002 | 26/50     | 0.9484 |
| k-means (espaço) − average linkage | acc       |  50 | -0.021 | 18/50     | 0.0918 |


| method              |   ('acc', 'cub_dinov2') |   ('acc', 'omniglot_dinov2') |   ('acc', 'omniglot_hog') |   ('acc', 'ts_Crop') |   ('acc', 'ts_NonInvasiveFetalECGThorax1') |   ('acc', 'ts_ShapesAll') |   ('acc', 'ts_SwedishLeaf') |
|:--------------------|------------------------:|-----------------------------:|--------------------------:|---------------------:|-------------------------------------------:|--------------------------:|----------------------------:|
| Ward (espaço)       |                   0.797 |                        0.718 |                     0.593 |                0.525 |                                      0.75  |                     0.668 |                       0.544 |
| average linkage (P) |                   0.736 |                        0.745 |                     0.56  |                0.56  |                                      0.768 |                     0.711 |                       0.608 |
| espectral (P)       |                   0.745 |                        0.699 |                     0.478 |                0.435 |                                      0.749 |                     0.627 |                       0.584 |
| k-means (espaço)    |                   0.788 |                        0.676 |                     0.565 |                0.52  |                                      0.762 |                     0.651 |                       0.528 |


### ponta a ponta

| comparação                         | métrica   |   n |    dif | a_favor   |      p |
|:-----------------------------------|:----------|----:|-------:|:----------|-------:|
| espectral (P) − average linkage    | test_all  |  50 |  0.001 | 21/50     | 0.7069 |
| espectral (P) − average linkage    | test_new  |  50 |  0.005 | 22/50     | 0.6267 |
| espectral (P) − average linkage    | new       |  50 | -0.027 | 10/50     | 0.0001 |
| Ward (espaço) − average linkage    | test_all  |  50 |  0     | 23/50     | 0.5116 |
| Ward (espaço) − average linkage    | test_new  |  50 |  0.007 | 23/50     | 0.3543 |
| Ward (espaço) − average linkage    | new       |  50 | -0.011 | 18/50     | 0.0886 |
| k-means (espaço) − average linkage | test_all  |  50 |  0     | 23/50     | 0.4126 |
| k-means (espaço) − average linkage | test_new  |  50 |  0.008 | 24/50     | 0.2608 |
| k-means (espaço) − average linkage | new       |  50 | -0.021 | 17/50     | 0.0139 |


| method              |   ('test_all', 'cub_dinov2') |   ('test_all', 'omniglot_dinov2') |   ('test_all', 'omniglot_hog') |   ('test_all', 'ts_Crop') |   ('test_all', 'ts_NonInvasiveFetalECGThorax1') |   ('test_all', 'ts_ShapesAll') |   ('test_all', 'ts_SwedishLeaf') |   ('test_new', 'cub_dinov2') |   ('test_new', 'omniglot_dinov2') |   ('test_new', 'omniglot_hog') |   ('test_new', 'ts_Crop') |   ('test_new', 'ts_NonInvasiveFetalECGThorax1') |   ('test_new', 'ts_ShapesAll') |   ('test_new', 'ts_SwedishLeaf') |   ('new', 'cub_dinov2') |   ('new', 'omniglot_dinov2') |   ('new', 'omniglot_hog') |   ('new', 'ts_Crop') |   ('new', 'ts_NonInvasiveFetalECGThorax1') |   ('new', 'ts_ShapesAll') |   ('new', 'ts_SwedishLeaf') |
|:--------------------|-----------------------------:|----------------------------------:|-------------------------------:|--------------------------:|------------------------------------------------:|-------------------------------:|---------------------------------:|-----------------------------:|----------------------------------:|-------------------------------:|--------------------------:|------------------------------------------------:|-------------------------------:|---------------------------------:|------------------------:|-----------------------------:|--------------------------:|---------------------:|-------------------------------------------:|--------------------------:|----------------------------:|
| Ward (espaço)       |                        0.807 |                             0.762 |                          0.612 |                     0.523 |                                           0.779 |                          0.789 |                            0.691 |                        0.732 |                             0.681 |                          0.514 |                     0.475 |                                           0.731 |                          0.702 |                            0.568 |                   0.676 |                        0.6   |                     0.446 |                0.377 |                                      0.689 |                     0.622 |                       0.603 |
| average linkage (P) |                        0.802 |                             0.755 |                          0.609 |                     0.527 |                                           0.781 |                          0.794 |                            0.709 |                        0.718 |                             0.655 |                          0.492 |                     0.49  |                                           0.723 |                          0.708 |                            0.608 |                   0.654 |                        0.615 |                     0.444 |                0.393 |                                      0.713 |                     0.639 |                       0.672 |
| espectral (P)       |                        0.804 |                             0.758 |                          0.609 |                     0.516 |                                           0.787 |                          0.798 |                            0.709 |                        0.724 |                             0.657 |                          0.494 |                     0.48  |                                           0.749 |                          0.712 |                            0.616 |                   0.654 |                        0.581 |                     0.377 |                0.377 |                                      0.684 |                     0.619 |                       0.667 |
| k-means (espaço)    |                        0.807 |                             0.757 |                          0.61  |                     0.527 |                                           0.781 |                          0.789 |                            0.702 |                        0.739 |                             0.658 |                          0.515 |                     0.5   |                                           0.723 |                          0.704 |                            0.592 |                   0.679 |                        0.569 |                     0.428 |                0.382 |                                      0.679 |                     0.621 |                       0.597 |


## 3. Sensibilidade no protocolo final (diferença para o padrão)

| fator        | valor          | métrica   |   n |    dif | a_favor   |      p |
|:-------------|:---------------|:----------|----:|-------:|:----------|-------:|
| agregação    | top1           | test_all  |  25 | -0.029 | 4/25      | 0.0008 |
| agregação    | top1           | test_new  |  25 | -0.042 | 6/25      | 0.0019 |
| agregação    | top1           | auroc     |  25 | -0.012 | 5/25      | 0.0023 |
| agregação    | top1           | disc_acc  |  25 |  0     | 0/25      | 1      |
| agregação    | top1           | k_err     |  25 |  0.4   | 12/25     | 0.6266 |
| agregação    | top5           | test_all  |  25 | -0.01  | 10/25     | 0.0542 |
| agregação    | top5           | test_new  |  25 | -0.001 | 11/25     | 0.7324 |
| agregação    | top5           | auroc     |  25 | -0.002 | 7/25      | 0.1135 |
| agregação    | top5           | disc_acc  |  25 |  0     | 0/25      | 1      |
| agregação    | top5           | k_err     |  25 |  2.56  | 9/25      | 0.8218 |
| agregação    | mean           | test_all  |  25 | -0.042 | 1/25      | 0      |
| agregação    | mean           | test_new  |  25 | -0.043 | 6/25      | 0.0036 |
| agregação    | mean           | auroc     |  25 | -0.016 | 3/25      | 0      |
| agregação    | mean           | disc_acc  |  25 |  0     | 0/25      | 1      |
| agregação    | mean           | k_err     |  25 |  3.92  | 8/25      | 0.063  |
| negativos    | 1:1            | test_all  |  25 | -0.004 | 9/25      | 0.1653 |
| negativos    | 1:1            | test_new  |  25 |  0.007 | 13/25     | 0.4832 |
| negativos    | 1:1            | auroc     |  25 | -0.011 | 5/25      | 0.0009 |
| negativos    | 1:1            | disc_acc  |  25 |  0.004 | 14/25     | 0.657  |
| negativos    | 1:1            | k_err     |  25 | 10     | 5/25      | 0.001  |
| negativos    | 5:1            | test_all  |  25 |  0.001 | 16/25     | 0.1422 |
| negativos    | 5:1            | test_new  |  25 |  0.006 | 12/25     | 0.6963 |
| negativos    | 5:1            | auroc     |  25 | -0.001 | 11/25     | 0.5965 |
| negativos    | 5:1            | disc_acc  |  25 | -0.005 | 11/25     | 0.6472 |
| negativos    | 5:1            | k_err     |  25 |  3.08  | 9/25      | 0.2292 |
| negativos    | difíceis (50%) | test_all  |  25 | -0.021 | 10/25     | 0.0395 |
| negativos    | difíceis (50%) | test_new  |  25 | -0.049 | 7/25      | 0.0502 |
| negativos    | difíceis (50%) | auroc     |  25 |  0.003 | 10/25     | 0.8949 |
| negativos    | difíceis (50%) | disc_acc  |  25 | -0.05  | 8/25      | 0.1094 |
| negativos    | difíceis (50%) | k_err     |  25 |  0.76  | 9/25      | 0.626  |
| PCA          | 128            | test_all  |  25 |  0.012 | 19/25     | 0.0118 |
| PCA          | 128            | test_new  |  25 |  0.015 | 15/25     | 0.3101 |
| PCA          | 128            | auroc     |  25 |  0.006 | 17/25     | 0.0081 |
| PCA          | 128            | disc_acc  |  25 |  0.019 | 13/25     | 0.2471 |
| PCA          | 128            | k_err     |  25 |  2.52  | 10/25     | 0.1956 |
| pseudo-novas | 15%            | test_all  |  25 | -0.009 | 6/25      | 0.0296 |
| pseudo-novas | 15%            | test_new  |  25 | -0.016 | 10/25     | 0.3524 |
| pseudo-novas | 15%            | auroc     |  25 |  0     | 0/25      | 1      |
| pseudo-novas | 15%            | disc_acc  |  25 | -0.01  | 13/25     | 0.9658 |
| pseudo-novas | 15%            | k_err     |  25 | -1.12  | 12/25     | 0.6809 |
| pseudo-novas | 40%            | test_all  |  25 |  0.003 | 12/25     | 0.5227 |
| pseudo-novas | 40%            | test_new  |  25 |  0.006 | 9/25      | 0.7033 |
| pseudo-novas | 40%            | auroc     |  25 |  0     | 0/25      | 1      |
| pseudo-novas | 40%            | disc_acc  |  25 |  0.029 | 17/25     | 0.0533 |
| pseudo-novas | 40%            | k_err     |  25 |  5.8   | 7/25      | 0.0105 |
| ligação      | single         | test_all  |  25 | -0.171 | 0/25      | 0      |
| ligação      | single         | test_new  |  25 | -0.512 | 0/25      | 0      |
| ligação      | single         | auroc     |  25 |  0     | 0/25      | 1      |
| ligação      | single         | disc_acc  |  25 | -0.59  | 0/25      | 0      |
| ligação      | single         | k_err     |  25 |  8.48  | 2/25      | 0      |
| ligação      | complete       | test_all  |  25 |  0.003 | 11/25     | 0.5426 |
| ligação      | complete       | test_new  |  25 | -0     | 8/25      | 0.5083 |
| ligação      | complete       | auroc     |  25 |  0     | 0/25      | 1      |
| ligação      | complete       | disc_acc  |  25 | -0.027 | 11/25     | 0.231  |
| ligação      | complete       | k_err     |  25 |  8.84  | 5/25      | 0.0003 |

### Médias

|                                               |   test_all |   test_new |   auroc |   disc_acc |   k_err |
|:----------------------------------------------|-----------:|-----------:|--------:|-----------:|--------:|
| ('padrão', 'top3 / 3:1 / 64 / 25% / average') |      0.781 |      0.691 |   0.864 |      0.735 |    7.44 |
| ('agregação', 'top1')                         |      0.752 |      0.649 |   0.852 |      0.735 |    7.84 |
| ('agregação', 'top5')                         |      0.772 |      0.69  |   0.862 |      0.735 |   10    |
| ('agregação', 'mean')                         |      0.74  |      0.648 |   0.848 |      0.735 |   11.36 |
| ('negativos', '1:1')                          |      0.777 |      0.698 |   0.853 |      0.738 |   17.44 |
| ('negativos', '5:1')                          |      0.782 |      0.696 |   0.863 |      0.73  |   10.52 |
| ('negativos', 'difíceis (50%)')               |      0.761 |      0.642 |   0.867 |      0.685 |    8.2  |
| ('PCA', '128')                                |      0.794 |      0.706 |   0.87  |      0.753 |    9.96 |
| ('pseudo-novas', '15%')                       |      0.773 |      0.674 |   0.864 |      0.724 |    6.32 |
| ('pseudo-novas', '40%')                       |      0.785 |      0.696 |   0.864 |      0.764 |   13.24 |
| ('ligação', 'single')                         |      0.61  |      0.179 |   0.864 |      0.145 |   15.92 |
| ('ligação', 'complete')                       |      0.785 |      0.69  |   0.864 |      0.708 |   16.28 |


## 4. SimGCD raso com o K̂ da dicotomia

| comparação                                         | métrica   |   n |    dif | a_favor   |      p |
|:---------------------------------------------------|:----------|----:|-------:|:----------|-------:|
| SimGCD (K da dicotomia) − proposto                 | test_all  |  50 |  0.062 | 44/50     | 0      |
| SimGCD (K da dicotomia) − SimGCD raso (K estimado) | test_all  |  50 |  0.026 | 28/50     | 0.0025 |
| SimGCD (K da dicotomia) − SimGCD raso (K oráculo)  | test_all  |  50 | -0.013 | 14/50     | 0.0014 |
| SimGCD (K da dicotomia) − proposto                 | test_new  |  50 |  0.05  | 35/50     | 0.0001 |
| SimGCD (K da dicotomia) − SimGCD raso (K estimado) | test_new  |  50 |  0.026 | 30/50     | 0.0416 |
| SimGCD (K da dicotomia) − SimGCD raso (K oráculo)  | test_new  |  50 | -0.019 | 17/50     | 0.0493 |
| SimGCD (K da dicotomia) − proposto                 | all       |  50 |  0.075 | 43/50     | 0      |
| SimGCD (K da dicotomia) − SimGCD raso (K estimado) | all       |  50 |  0.042 | 31/50     | 0.0077 |
| SimGCD (K da dicotomia) − SimGCD raso (K oráculo)  | all       |  50 | -0.042 | 5/50      | 0      |
| SimGCD (K da dicotomia) − proposto                 | new       |  50 |  0.077 | 40/50     | 0      |
| SimGCD (K da dicotomia) − SimGCD raso (K estimado) | new       |  50 |  0.038 | 30/50     | 0.0169 |
| SimGCD (K da dicotomia) − SimGCD raso (K oráculo)  | new       |  50 | -0.045 | 12/50     | 0      |


| ds                            |   test_all |   test_new |   all |   new |
|:------------------------------|-----------:|-----------:|------:|------:|
| cub_dinov2                    |      0.846 |      0.727 | 0.822 | 0.722 |
| omniglot_dinov2               |      0.852 |      0.751 | 0.825 | 0.742 |
| omniglot_hog                  |      0.702 |      0.57  | 0.659 | 0.553 |
| ts_Crop                       |      0.53  |      0.5   | 0.459 | 0.445 |
| ts_NonInvasiveFetalECGThorax1 |      0.835 |      0.749 | 0.798 | 0.762 |
| ts_ShapesAll                  |      0.825 |      0.746 | 0.75  | 0.688 |
| ts_SwedishLeaf                |      0.771 |      0.664 | 0.764 | 0.688 |


## 5. SimGCD: K da dicotomia aprendida vs. K da distância fixa

| comparação                     | métrica   |   n |   dif | a_favor   |      p |
|:-------------------------------|:----------|----:|------:|:----------|-------:|
| K aprendido − K distância fixa | test_all  |  50 | 0.022 | 33/50     | 0.0006 |
| K aprendido − K distância fixa | test_new  |  50 | 0.038 | 31/50     | 0.0012 |
| K aprendido − K distância fixa | all       |  50 | 0.033 | 26/50     | 0.0321 |
| K aprendido − K distância fixa | new       |  50 | 0.045 | 35/50     | 0.0013 |


| ds                            |   test_all |   test_new |   k_est |
|:------------------------------|-----------:|-----------:|--------:|
| cub_dinov2                    |      0.847 |      0.732 |    26.1 |
| omniglot_dinov2               |      0.817 |      0.706 |    44.9 |
| omniglot_hog                  |      0.697 |      0.525 |    20.9 |
| ts_Crop                       |      0.498 |      0.47  |    17.2 |
| ts_NonInvasiveFetalECGThorax1 |      0.817 |      0.726 |    16.4 |
| ts_ShapesAll                  |      0.774 |      0.684 |    31.4 |
| ts_SwedishLeaf                |      0.727 |      0.568 |     6.6 |

