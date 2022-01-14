
fichier = "/home/vagrant/prenoms.txt"
fichier_de_sortie = "/home/vagrant/prenoms_reformate.txt"

with open(fichier, mode="r") as f:
    #contenu = f.read()
    contenu = f.read().split()
    contenu.sort()
    a_la_ligne = "\n".join(contenu)    
    
    for prenom in a_la_ligne:
        prenom.strip(",. ")    
   
    with open(fichier_de_sortie, "w") as f:        
        f.write(a_la_ligne.replace(",", ""))
    
    
        




