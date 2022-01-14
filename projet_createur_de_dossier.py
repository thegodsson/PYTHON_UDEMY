from pathlib import Path

donnes = {

      ".avi":"Films",
      ".mp3":"Musiques",
      ".mp4":"Films",
      ".png":"Images",
      ".txt":"Documents"

}

source = Path.home() / "Download"

fichiers = [f for f in source.iterdir() if f.is_file()]

#print(fichiers)

for f in fichiers:
    rep_acrerr = source / donnes.get(f.suffix, "Autres")
    rep_acrerr.mkdir(exist_ok=True)
    f.rename(rep_acrerr / f.name)


