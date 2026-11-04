"""Embeddings DINOv2 congelados para o CUB-200-2011, com os splits do Semantic Shift Benchmark.

O CUB tem 200 espécies de aves (11.788 imagens, 41 a 60 por classe). O Semantic Shift
Benchmark (Vaze et al., ICLR 2022) fixa 100 classes conhecidas e divide as outras 100
em Easy (32), Medium (34) e Hard (34), conforme quantos atributos compartilham com as
conhecidas. Hard = mais parecidas com as conhecidas, Easy = mais diferentes. Por isso,
no nosso protocolo: near = Hard e far = Easy (Medium não é usado).

O campo `split` do .npz recebe o grupo de cada imagem ("known", "easy", "medium", "hard");
experiments.py reconhece esse formato e sorteia as classes novas no grupo certo.

Uso:
    python features_cub.py data cub_dinov2.npz            # baixa o CUB (1,1 GB) se faltar
    python features_cub.py data cub_dinov2.npz --model dinov2_vitb14

Como no Omniglot, a rede NÃO é ajustada. A GPU (MPS no Mac) só acelera esta extração
única (~12 mil imagens, poucos minutos); todo o resto roda em CPU.
"""
import argparse
import json
import os
import tarfile
import time
import urllib.request
from pathlib import Path

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import numpy as np
import torch
from PIL import Image

from features_cnn import MEAN, STD, load_model, pick_device

URL = "https://data.caltech.edu/records/65de6-vp158/files/CUB_200_2011.tgz"
SPLITS = Path(__file__).parent / "data" / "ssb_cub_splits.json"


def get_cub(root: Path) -> Path:
    cub = root / "CUB_200_2011"
    if (cub / "images.txt").exists():
        return cub
    root.mkdir(parents=True, exist_ok=True)
    tgz = root / "CUB_200_2011.tgz"
    if not tgz.exists():
        print(f"baixando {URL} (1,1 GB)...", flush=True)
        # O CaltechDATA recusa (403) o User-Agent padrão do urllib; usamos um de navegador.
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
        part = tgz.with_suffix(".tgz.part")
        with urllib.request.urlopen(req) as r, open(part, "wb") as f:
            total, done = int(r.headers.get("Content-Length", 0)), 0
            while chunk := r.read(1 << 20):
                f.write(chunk); done += len(chunk)
                if total and done % (50 << 20) < (1 << 20):
                    print(f"  {done / 2**20:.0f} / {total / 2**20:.0f} MB", flush=True)
        part.rename(tgz)
        # Se ainda falhar, baixe pelo navegador e coloque o arquivo em data/CUB_200_2011.tgz.
    print("extraindo...", flush=True)
    with tarfile.open(tgz) as t:
        t.extractall(root)
    return cub


def list_cub(cub: Path):
    """Caminhos, rótulos 0..199 (class_id - 1, como no SSB) e grupo SSB de cada imagem."""
    paths = dict(l.split() for l in (cub / "images.txt").read_text().splitlines())
    labels = dict(l.split() for l in (cub / "image_class_labels.txt").read_text().splitlines())
    groups = json.loads(SPLITS.read_text())
    group_of = {c: g for g, cs in groups.items() for c in cs}
    ids = sorted(paths, key=int)
    P = [cub / "images" / paths[i] for i in ids]
    y = np.array([int(labels[i]) - 1 for i in ids])
    g = np.array([group_of[c] for c in y])
    return P, y, g


def to_tensor(path, size=224):
    """RGB, lado menor redimensionado para 256 e recorte central 224 (padrão ImageNet)."""
    img = Image.open(path).convert("RGB")
    w, h = img.size
    s = 256 / min(w, h)
    img = img.resize((round(w * s), round(h * s)), Image.BICUBIC)
    w, h = img.size
    l, t = (w - size) // 2, (h - size) // 2
    img = img.crop((l, t, l + size, t + size))
    x = torch.from_numpy(np.asarray(img, dtype=np.float32) / 255.0).permute(2, 0, 1)
    return (x - torch.tensor(MEAN)[:, None, None]) / torch.tensor(STD)[:, None, None]


@torch.inference_mode()
def extract(paths, model, batch, device):
    out, t0 = [], time.time()
    for i in range(0, len(paths), batch):
        xb = torch.stack([to_tensor(p) for p in paths[i:i + batch]])
        out.append(model(xb.to(device)).float().cpu().numpy())
        if (i // batch) % 20 == 0:
            done = i + len(xb)
            eta = (time.time() - t0) / done * (len(paths) - done)
            print(f"  {done}/{len(paths)}  ~{eta / 60:.1f} min restantes", flush=True)
    return np.vstack(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path, help="pasta onde o CUB está (ou será baixado)")
    ap.add_argument("out")
    ap.add_argument("--model", default="dinov2_vits14", choices=["dinov2_vits14", "dinov2_vitb14"])
    ap.add_argument("--device", default="auto")
    ap.add_argument("--batch", type=int, default=64)
    args = ap.parse_args()
    cub = get_cub(args.root)
    paths, y, g = list_cub(cub)
    model, _ = load_model(args.model)
    device = pick_device(args.device)
    model.eval().to(device)
    print(f"{len(paths)} imagens, {len(np.unique(y))} classes, modelo {args.model}, dispositivo {device}")
    print({k: len(np.unique(y[g == k])) for k in ("known", "easy", "medium", "hard")}, "classes por grupo")
    X = extract(paths, model, args.batch, device)
    np.savez_compressed(args.out, X=X.astype(np.float32), y=y, split=g)
    print(X.shape, "->", args.out)
