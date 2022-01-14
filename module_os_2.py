import os
chemin = "D:/UDEMY_1_THIBAULT/Section_12"
dossier_a_creer = os.path.join(chemin, "dossier2", "test1")

if not os.path.exists(dossier_a_creer):
    print("LE DOSIER NEXISTE PAS")
    print(f"CREATION DU DOSSIER {dossier_a_creer}")
    os.makedirs(dossier_a_creer)
else:
    print("LE DOSSIER EXISTE DEJA")

