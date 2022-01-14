chemin = "/home/vagrant/fichier.txt"


"""
with open(chemin, "w") as f:    
    #contenu = f.write("Bonjour") # --> Efface ce qui est déja dans le fichier
"""
    
with open(chemin, "a") as f:    
    #contenu = f.write("Bonjour") # --> Ajoute sans effacerdans le fichier
    contenu = f.write("\nAu revoir") # --> mettre à la ligne


    