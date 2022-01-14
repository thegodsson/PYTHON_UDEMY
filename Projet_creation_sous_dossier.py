
from pathlib import Path

chemin = "/home/vagrant/DOSSIER_TEST"

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


#print(source)

for dossiers_pricipal, sous_dossiers in d.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(chemin) / dossiers_pricipal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)
        
        
        
    
    