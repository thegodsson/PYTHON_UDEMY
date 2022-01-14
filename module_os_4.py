from genericpath import exists
import os
chemin = "D:/UDEMY_1_THIBAULT/Section_12"
dossier_a_creer = os.path.join(chemin, "dossier2", "test1")

#os.makedirs(dossier_a_creer, exist_ok=True)


if os.path.exists(dossier_a_creer):
    print("Dossier existant")
    print("Suppression")
    os.removedirs(dossier_a_creer)
else:
    print("Déja supprimé")
