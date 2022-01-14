from pathlib import Path

p = Path("/home/vagrant/Documents/index.tar.gz")

print(p.name)
print(p.parent)
print(p.stem)
print(p.suffix)
print(p.suffixes)
print(p.parts)
print(p.exists())
print(p.is_dir())
print(p.is_file())

print(p.parent.parent)