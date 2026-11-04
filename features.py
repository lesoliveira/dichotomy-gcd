"""Extração de características (CPU) para o Omniglot.

Cada caractere é um "classe" (964 no background, 659 no evaluation), 20 amostras cada.
Representação: HOG sobre a imagem reduzida para 48x48, seguida de PCA (ajustado só
nas classes conhecidas, dentro do experimento). Aqui salvamos apenas o HOG bruto.

Uso:
    python features.py <pasta_omniglot> <saida.npz>
"""
import sys
from pathlib import Path

import numpy as np
from joblib import Parallel, delayed
from skimage.feature import hog
from skimage.io import imread
from skimage.transform import resize


def _feat(path):
    img = imread(path, as_gray=True).astype(np.float32)
    img = 1.0 - img  # traço = 1
    img = resize(img, (48, 48), anti_aliasing=True)
    return hog(img, orientations=9, pixels_per_cell=(8, 8),
               cells_per_block=(2, 2), feature_vector=True)


def list_images(root: Path):
    """Caminhos, rótulo de caractere, alfabeto e parte (background/evaluation)."""
    paths, labels, alphabets, split = [], [], [], []
    cls = 0
    for part in ("images_background", "images_evaluation"):
        for alpha in sorted((root / part).iterdir()):
            for char in sorted(alpha.iterdir()):
                for p in sorted(char.glob("*.png")):
                    paths.append(p)
                    labels.append(cls)
                    alphabets.append(f"{part}/{alpha.name}")
                    split.append(part)
                cls += 1
    return paths, np.array(labels), np.array(alphabets), np.array(split)


def build(root: Path):
    paths, labels, alphabets, split = list_images(root)
    X = np.vstack(Parallel(n_jobs=-1, batch_size=256)(delayed(_feat)(p) for p in paths))
    return X.astype(np.float32), labels, alphabets, split


if __name__ == "__main__":
    root, out = Path(sys.argv[1]), sys.argv[2]
    X, y, a, s = build(root)
    np.savez_compressed(out, X=X, y=y, alphabet=a, split=s)
    print(X.shape, len(np.unique(y)), "classes")
