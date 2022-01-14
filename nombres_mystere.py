
import random


nombre_generer = random.randint(0, 100)
print(nombre_generer)

essaie = 5


while essaie > 0:

    print("Le jeu du nombre mystère")
    print(f"Il te reste {essaie} essais ")

    

    nbr_a_deviner = input("Devine le nombre : ")     
    
    if nbr_a_deviner.isdigit():
        nbr_a_deviner = int(nbr_a_deviner)

        if nbr_a_deviner > nombre_generer:
            print(f"Le nombre mystère est plus petit que {nbr_a_deviner}")
            essaie -= 1
            if essaie < 1:
                print(f"Dommage ! Le nombre mystère était {nombre_generer} \n Fin du Jeu")           
        elif nbr_a_deviner < nombre_generer:
            print(f"Le nombre mystère est plus grand que {nbr_a_deviner}")
            essaie -= 1
            if essaie < 1:
                print(f"Dommage ! Le nombre mystère était {nombre_generer} \nFin du Jeu")        
            continue
    
        elif nbr_a_deviner == nombre_generer:
            print(f"Bravo ! Le nombre mystère était bien {nombre_generer} !\nTu as trouvé le nombre en {essaie} essai\nFin du jeu.")
            break
    
    else:
        print("Ce n'est pas un nombre")
        continue