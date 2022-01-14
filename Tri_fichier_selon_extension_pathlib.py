from pathlib import Path

dirs = {".png": "Images",
        ".avi": "Films",
        ".pdf": "Documents",
        ".jpeg": "Images",
        ".txt": "Documents",
        ".mp4": "Films"}


tri_dir = Path.home() / "Download"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

