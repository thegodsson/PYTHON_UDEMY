from os import path, read
from pathlib import Path

import shutil

p = Path.home()

p = p / "DossierTest"

p.mkdir(exist_ok=True)

p = p / "1" / "2" / "3"

#p.mkdir(parents=True)

#p = p / "readme.txt"

#p.touch()
#p.unlink()   #Suppréssion du fichier

p = p.parent.parent.parent

shutil.rmtree(p)

#print(p)

#p.rmdir()


