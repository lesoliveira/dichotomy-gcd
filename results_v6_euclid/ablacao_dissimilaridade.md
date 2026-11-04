# Ablação: dissimilaridade aprendida (hgb) vs. distância euclidiana calibrada

Para k_err, menor é melhor (diferença negativa favorece A).

| grupo                         | A                        | B                      | métrica   |   n |   dif | A_vence   |      p |
|:------------------------------|:-------------------------|:-----------------------|:----------|----:|------:|:----------|-------:|
| todos                         | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |  40 | 0.034 | 30/40     | 0.0004 |
| omniglot_dinov2               | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |  10 | 0.056 | 10/10     | 0.002  |
| omniglot_hog                  | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |  10 | 0.001 | 5/10      | 0.9414 |
| ts_Crop                       | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |   5 | 0.023 | 3/5       | 0.625  |
| ts_NonInvasiveFetalECGThorax1 | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |   5 | 0.064 | 5/5       | 0.0625 |
| ts_ShapesAll                  | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |   5 | 0.06  | 4/5       | 0.125  |
| ts_SwedishLeaf                | dicotomia-euclid + ruído | SS-kmeans (K estimado) | test_all  |   5 | 0.011 | 3/5       | 0.875  |