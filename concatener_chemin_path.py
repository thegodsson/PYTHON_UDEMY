from pathlib import Path, PosixPath
p = Path.home()
print(p / "Documents")
print((p / "Documents" / "main.py").suffix)
print(p.joinpath("Documents", "main.py"))
print(p.joinpath("Documents", "main.py").suffix)