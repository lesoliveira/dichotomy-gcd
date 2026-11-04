"""Embeddings de redes pré-treinadas para o Omniglot (GPU Apple/MPS, CUDA ou CPU).

As redes NÃO são ajustadas: extraímos o embedding uma única vez e todo o resto
(dichotomizer, calibração, clustering) continua raso e em CPU. A GPU só acelera
esta extração; o método em si não depende dela.

Modelos:
  dinov2_vits14  ViT-S/14 auto-supervisionado (Meta, 2023), CLS de 384-d. Recomendado:
                 auto-supervisionado, sem rótulos do ImageNet -> menos "vazamento" de classes.
  dinov2_vitb14  ViT-B/14, 768-d. Mais forte; viável com GPU.
  resnet50       ImageNet-1k supervisionado (torchvision), 2048-d.
  resnet18       ImageNet-1k supervisionado (torchvision), 512-d. O mais rápido.

Uso:
    python features_cnn.py <pasta_omniglot> omniglot_dinov2.npz --model dinov2_vits14
    python features_cnn.py <pasta_omniglot> omniglot_resnet50.npz --model resnet50

Dispositivo: --device auto escolhe mps (Mac Apple Silicon) > cuda > cpu.
Tempo aproximado (32.460 imagens): com GPU do Mac, poucos minutos para qualquer modelo;
só CPU: resnet18 ~3-6 min | dinov2_vits14 ~8-20 min | resnet50 ~10-25 min.
Na primeira execução os pesos são baixados (dinov2 ~90 MB via torch.hub/GitHub).
"""
import argparse
import os
import time
from pathlib import Path

os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")  # ops sem suporte MPS caem p/ CPU

import numpy as np
import torch
from PIL import Image

from features import list_images

MEAN, STD = (0.485, 0.456, 0.406), (0.229, 0.224, 0.225)


def pick_device(name):
    if name != "auto":
        return torch.device(name)
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def load_model(name):
    if name.startswith("dinov2"):
        m = torch.hub.load("facebookresearch/dinov2", name)
        return m, 224                       # forward() devolve o token CLS normalizado
    import torchvision
    if name == "resnet50":
        m = torchvision.models.resnet50(weights="IMAGENET1K_V2")
    elif name == "resnet18":
        m = torchvision.models.resnet18(weights="IMAGENET1K_V1")
    else:
        raise ValueError(name)
    m.fc = torch.nn.Identity()              # saída = pooling global
    return m, 224


def to_tensor(path, size):
    # Omniglot: traço preto em fundo branco, 105x105, 1 canal -> RGB 224x224
    img = Image.open(path).convert("L").resize((size, size), Image.BICUBIC).convert("RGB")
    x = torch.from_numpy(np.asarray(img, dtype=np.float32) / 255.0).permute(2, 0, 1)
    return (x - torch.tensor(MEAN)[:, None, None]) / torch.tensor(STD)[:, None, None]


@torch.inference_mode()
def extract(paths, model, size, batch, device):
    out = []
    t0 = time.time()
    for i in range(0, len(paths), batch):
        xb = torch.stack([to_tensor(p, size) for p in paths[i:i + batch]])
        out.append(model(xb.to(device)).float().cpu().numpy())
        if (i // batch) % 20 == 0:
            done = i + len(xb)
            eta = (time.time() - t0) / done * (len(paths) - done)
            print(f"  {done}/{len(paths)}  ~{eta / 60:.1f} min restantes", flush=True)
    return np.vstack(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("out")
    ap.add_argument("--model", default="dinov2_vits14",
                    choices=["dinov2_vits14", "dinov2_vitb14", "resnet50", "resnet18"])
    ap.add_argument("--device", default="auto", help="auto | mps | cuda | cpu")
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--threads", type=int, default=os.cpu_count())
    ap.add_argument("--random-weights", action="store_true",
                    help="só para testar o código sem baixar pesos (resnet)")
    args = ap.parse_args()
    torch.set_num_threads(args.threads)
    if args.random_weights:
        import torchvision
        model = getattr(torchvision.models, args.model)(weights=None)
        model.fc, size = torch.nn.Identity(), 224
    else:
        model, size = load_model(args.model)
    device = pick_device(args.device)
    model.eval().to(device)
    paths, y, alpha, split = list_images(args.root)
    print(f"{len(paths)} imagens, modelo {args.model}, dispositivo {device}")
    X = extract(paths, model, size, args.batch, device)
    np.savez_compressed(args.out, X=X.astype(np.float32), y=y, alphabet=alpha, split=split)
    print(X.shape, len(np.unique(y)), "classes ->", args.out)
