from pathlib import Path

# iterdir --> permet de listé tout ce qui se trouve dans un dossier
p = Path.home().iterdir()


"""
for f in p:
    print(f.name)
"""


dossier = [f for f in Path.home().iterdir() if f.is_dir()]
fichier = [f for f in Path.home().iterdir() if f.is_file()]
print(f"Dossiers : {dossier}")
print("----------------------------")
print(f"Fichiers : {fichier}")


"""
p = Path.home() / "Download"

p.mkdir(exist_ok=True)

#fichier_png = [ f for f in p.glob("*.png") if f.name]
fichier_png = [ f for f in p.rglob("*.png") if f.name]

print(fichier_png)

"""