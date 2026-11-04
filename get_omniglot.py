"""Baixa e extrai o Omniglot (github.com/brendenlake/omniglot) para ./data/omniglot."""
import urllib.request
import zipfile
from pathlib import Path

BASE = "https://raw.githubusercontent.com/brendenlake/omniglot/master/python/"
dest = Path(__file__).parent / "data" / "omniglot"
dest.mkdir(parents=True, exist_ok=True)
for name in ("images_background", "images_evaluation"):
    if (dest / name).exists():
        print(f"{name}: já existe"); continue
    z = dest / f"{name}.zip"
    print(f"baixando {name}.zip ...")
    urllib.request.urlretrieve(BASE + f"{name}.zip", z)
    zipfile.ZipFile(z).extractall(dest)
    z.unlink()
print("ok ->", dest)
