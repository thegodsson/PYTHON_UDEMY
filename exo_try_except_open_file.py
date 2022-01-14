
fichier = input("Entrez un fichier à ouvrir : ")

try:
    with open(fichier, "r") as f:
        contenu = f.read()    
    print(contenu)
except FileNotFoundError:
    print("Fichier introuvable")
except UnicodeDecodeError as e:
    print("Erreur : ", e)


