#Clé valeur

d = {

      0: {"prenom": "Paul",
          "profession": "Ingénieur",
          "ville": "Paris"},
    
      1: {"prenom": "Julie",
          "profession": "Architecte",
          "ville": "Marseille"},

      2: {"prenom": "Pierre",
          "profession": "Plombier",
          "ville": "Nantes"},

}

#print(d[0]["prenom"]) #Vas nous retourné une erreur si la clé n'existe pas, cependant (get) renvoi "None"
print(d.get("prenom", "La clé 'prenom' n'existe pas"))