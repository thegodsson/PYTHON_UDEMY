
employes = {

    "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
    "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
    "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36},
    
    
}


for cles in employes:
    if "id03" in cles:
        del employes["id03"]

for cles, valeurs in employes.items():
    print(cles, valeurs)