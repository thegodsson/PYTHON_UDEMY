from pathlib import Path

print(Path.home())
print(Path.cwd())

p = Path("/home/vagrant")
print(p.parent)