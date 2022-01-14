import os

def verifier_fichier():
    return os.path.exists("fichier.txt")

print(verifier_fichier())