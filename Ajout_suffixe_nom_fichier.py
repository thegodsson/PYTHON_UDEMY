from pathlib import Path

p = Path.home() / "image.png"

print(p)

print(p.parent / (p.stem + "-lowers" + p.suffix))