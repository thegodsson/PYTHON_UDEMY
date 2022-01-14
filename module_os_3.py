import os
chemin = "D:/UDEMY_1_THIBAULT/Section_12"
dossier_a_creer = os.path.join(chemin, "dossier2", "test1")

os.makedirs(dossier_a_creer, exist_ok=True)
 