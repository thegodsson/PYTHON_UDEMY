
import random

pt_vies_user1 = 50
pt_vies_ennemi = 50
potion_user1 = 3



while pt_vies_user1 or pt_vies_ennemi > 0:
    
    valeur_potions = random.randint(15, 50)
    attaque_user1 = random.randint(5, 10)
    attaque_ennemi = random.randint(5, 15)

    reponse = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) : ")

    if reponse == "1":
        print(f"Vous avez infligé {attaque_user1} de dégats à l'ennemi")
        print(f"L'ennemi vous a infligé {attaque_ennemi} de dégats")
        pt_vies_user1 = pt_vies_user1 - attaque_ennemi
        pt_vies_ennemi = pt_vies_ennemi - attaque_user1
        print(f"Il vous reste {pt_vies_user1} points de vie.")
        print(f"Il reste {pt_vies_ennemi} de vie à l'ennemi.")
        print("---------------------------------------------------")

        if pt_vies_user1 <= 0:
            print("Vous avez perdu")
            break
        elif pt_vies_ennemi <= 0:
            print("Vous avez gagné")
            break            
        
    
    if reponse == "2":
        if potion_user1 == 0:
            print("Vous n'avez plus de potion ...")
            continue    
        pt_vies_user1 = pt_vies_user1 + valeur_potions
        pt_vies_user1 = pt_vies_user1 - attaque_ennemi                
        potion_user1 -= 1        
        print(f"Vous récupérer {valeur_potions} points de vies ({potion_user1} potions restantes) ")
        print(f"L'ennemi vous a infligé {attaque_ennemi} de dégats")
        print(f"Il vous reste {pt_vies_user1} points de vie.")
        print(f"Il reste {pt_vies_ennemi} de vie à l'ennemi.")
        print("---------------------------------------------------")
        attaque_ennemi = random.randint(5, 15)
        pt_vies_user1 = pt_vies_user1 - attaque_ennemi 
        print("Vous passez votre tour ...")
        print(f"L'ennemi vous a infligé {attaque_ennemi} de dégats")
        print(f"Il vous reste {pt_vies_user1} points de vie.")
        print(f"Il reste {pt_vies_ennemi} de vie à l'ennemi.")
        
        if pt_vies_user1 <= 0:
            print("Vous avez perdu")
            break
        elif pt_vies_ennemi <= 0:
            print("Vous avez gagné")
            break            
                
    else:
        continue
        
                



