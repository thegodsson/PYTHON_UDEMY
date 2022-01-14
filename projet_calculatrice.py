

while True:
    nombre1 = input("Entrer un premier nombre : ")
    nombre2 = input("Entrer un deuxieme nombre : ")
    
    if nombre1.isdigit() and nombre2.isdigit():
        resultat = int(nombre1) + int(nombre2)        
        print(f"Le résulat de l'addition de {nombre1} avec {nombre2} est égal à {resultat}")
        break
    else:
        print("Veuillez entrer deux nombres valides")
        continue