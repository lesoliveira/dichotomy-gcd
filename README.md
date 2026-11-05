# How Many Novel Classes? Estimating K for Generalized Category Discovery with a Learned Dichotomy

Code and results for the paper under double-blind review. Everything runs on a CPU; a GPU
is used only, if present, to extract the frozen DINOv2 features.

The method learns a dissimilarity from the known classes (the dichotomy transformation
z(a,b) = [|a−b|, a⊙b] fed to a gradient-boosting dichotomizer), calibrates its rejection
threshold, dendrogram cut and minimum cluster size on pseudo-novel classes held out from the
known ones, discovers the novel classes by average linkage on 1 − P(same), and either keeps
them as a prototype bank or hands the estimated K̂ to a SimGCD head.

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Python ≥ 3.10. `torch`/`torchvision` are needed only for the DINOv2 features
(`features_cnn.py`, `features_cub.py`); `aeon` only for the UCR series and MiniRocket.

## Data

All datasets are downloaded by the scripts:

| Dataset | Script | Features |
|---|---|---|
| Omniglot (background + evaluation) | `get_omniglot.py` → `data/omniglot` | HOG (`features.py`), DINOv2 ViT-S/14 (`features_cnn.py`) |
| CUB-200-2011 | `features_cub.py` → `data/CUB_200_2011` | DINOv2 ViT-S/14; SSB splits in `data/ssb_cub_splits.json` |
| UCR: ShapesAll, NonInvasiveFetalECGThorax1, Crop, SwedishLeaf | `features_ts.py` (via `aeon`) | MiniRocket |

Each feature file is an `.npz` in the repository root (`omniglot_dinov2.npz`, `ts_Crop.npz`, …).

## Reproducing the paper

```bash
bash reproduce.sh        # everything, in order (about one to two days on a laptop CPU)
```

or stage by stage:

| Stage | Command | Output | Paper |
|---|---|---|---|
| Main experiment and scale, no whitening | `bash run_v6.sh all` | `results_v6/<set>/` | K̂ error and accuracy tables, scale figure |
| Transfer of the learned similarity (RQ1) | `experiments.py --only transfer --transfer-clf hgb` (see `reproduce.sh`) | `results_v6/<set>/transferencia_hgb.csv` | transfer figure (RQ1) |
| Same runs with PCA whitening | `bash run_v5.sh` | `results_v5/<set>/` | baselines (best of both) |
| Fixed-distance ablation | `bash run_ablation_euclid.sh`, `bash run_euclid_whiten.sh` | `results_v6_euclid*/` | learned vs. fixed distance table |
| CUB-200-2011 (all of the above) | `bash run_cub.sh` | `results_v*/cub_dinov2/` | CUB rows |
| Final tables and Wilcoxon tests | `python final_tables.py` | `results_final/tabelas.md` | K̂ error, accuracy and ablation tables |
| SimGCD head, clustering alternatives, sensitivity | `bash run_review.sh` | `results_review/revisao.md` | SimGCD comparison, sensitivity table |
| SimGCD with K̂ from the dichotomy / fixed distance | `bash run_simgcd_khat.sh`, `bash run_simgcd_keuclid.sh` | `results_review/<set>/` | main SimGCD result (75.0 → 77.6, oracle 78.9) |
| Sensitivity to the number of novel classes K | `bash run_vary_k.sh` | `results_vary_k/` | K̂ vs. K (additional experiment) |
| Figures | `python make_figures.py`, `python make_dataset_figure.py`, `python fig_dendrogram.py` | `figures/` | transfer, scale, dataset examples, dendrogram |

Evaluation seeds are 20–24; with 10 splits per seed this gives the 50 paired runs used in the
Wilcoxon tests (`stats.py`). Run `bash run_v6.sh series` or `bash run_v6.sh omniglot` to do
only part of the main experiment (about 1 h and 3 h, respectively).

## Code

| File | Content |
|---|---|
| `dichotomy_owl.py` | the method: dichotomizer, calibration on pseudo-novel classes, out-of-fold threshold, discovery, noise rule, prototype bank |
| `experiments.py` | splits (near/far/random novelty), baselines (SS-k-means with K by grid search, etc.), main / scale / transfer experiments |
| `experiments_review.py` | shallow SimGCD head on frozen features, clustering alternatives, sensitivity analysis |
| `features*.py`, `get_omniglot.py` | data download and feature extraction |
| `final_tables.py`, `review_tables.py`, `summarize.py`, `compare_ablation.py`, `choose_prep.py`, `stats.py` | tables and statistical tests |
| `make_figures.py`, `make_dataset_figure.py`, `fig_dendrogram.py`, `plot_scale.py` | figures |

## Results included

All CSV and Markdown result files used in the paper are included, so tables and figures can be
regenerated without rerunning the experiments (`python final_tables.py`, `python make_figures.py`).
File names are in Portuguese: `deteccao` (detection), `descoberta` (discovery), `transferencia`
(transfer), `escala` (scale), `agrupamento` (clustering), `ablacao` (ablation), `tabelas`
(tables), `revisao` (review experiments). Some code comments are also in Portuguese.

Note on `results_v5`: only the whitened **baselines** in this folder are used in the paper
(each baseline receives the better of the whitened and non-whitened runs). The rows of the
proposed method in `results_v5` come from an earlier version of the code (5 out-of-fold
folds instead of 10) and are not reported.

## License

MIT, see `LICENSE`.
