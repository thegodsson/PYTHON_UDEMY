import json   #--> module json

chemin = "/home/vagrant/fichier.json"

"""
#Pour ecrire   
with open(chemin, "w") as f:    
    #json.dump("Bonjour", f)
    #json.dump(list(range(10)), f) # --> avec une liste mais pas lisible
    json.dump(list(range(10)), f, indent=4) #--> plus lisible avec une indentation de 4
"""

#Pour lire
with open(chemin, "r") as f:    
    liste = json.load(f)
    print(liste)
    print(type(liste))