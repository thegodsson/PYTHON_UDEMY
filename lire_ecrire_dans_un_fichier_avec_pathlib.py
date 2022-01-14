from pathlib import Path

p = Path.home() / "PathLib"

p.mkdir(exist_ok=True, parents=True)

p = Path.home() / "PathLib" / "readme.txt"

p.touch()

print(p)

p.write_text("Bonjour Les Amis")
p.read_text()