
#prenoms = ["Pierre", "Patrick", "Jean", "Marc"]
prenoms = ["Pierre", "Jean", "Marc"]

for prenom in prenoms:
    if prenom == "Patrick":
        print("Patrick à été trouvé !")
        break
else:
    print("Patrick est introuvable ...")