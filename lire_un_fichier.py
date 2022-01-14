chemin = "/home/vagrant/fichier.txt"

"""
#Premiere facon

f = open(chemin, "r")
f.close()
print(f)
"""
#Deuxieme facon le plus souvent utilisé et conseilé
with open(chemin, "r") as f:
    #contenu = f.read() #Vas lire le fichier tel qu'il est 
    #contenu = repr(f.read()) #--> vas mettre en forme le fichier lors de la lecture
    #contenu = f.readlines() #permet de récupérer les donnés dans une liste, cependant on récupère également les caractères don les saut de ligne -- \n
    contenu = f.read().splitlines() #permet de récupérer les donnés dans une liste, mais sans problèmes de caractères comme les \n


    print(contenu)

