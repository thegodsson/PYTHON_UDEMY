import json
from pathlib import Path
import subprocess

fichier = Path('/home/vagrant/liste_de_course.json')
fichier.touch(exist_ok=True)
fichier = "/home/vagrant/liste_de_course.json"


with open(fichier, "r") as f:    
    contenu = f.read()   
 
    if "[]" in contenu or len(contenu) > 0:
        pass
    else:        
        subprocess.run(['echo [] > /home/vagrant/liste_de_course.json'], shell=True)


with open("/home/vagrant/liste_de_course.json", "r") as f:    
            save_liste_course = json.load(f)


liste_de_course = save_liste_course
liste_de_course = list(liste_de_course)                 
        

while True:   
    print("----------------------------------------------")
    print("Choisissez parmi les 5 options suivantes : ")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    reponse = input("Votre choix : ")

    if reponse == "1":        
        ajout = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        if ajout in liste_de_course:
            print("Cet article est déja dans la liste de courses")
        else:
            liste_de_course.append(ajout)
            print(f"L'élément {ajout} a bien été ajouté à la liste")
        continue

    if reponse == "2":
        retirer = input("Entrez le nom d'un élément à retirer à la liste de courses : ")

        if retirer in liste_de_course:
            print(f"L'article {retirer} vas être supprimé de la liste de courses")            
            liste_de_course.remove(retirer)
            save_liste_course.remove(retirer)
        else:
            print(f"L'article {retirer} n'est pas dans la liste")
       
        continue

    if reponse == "3":
                  
        if len(liste_de_course) > 0:          
                  
            print("Voici le contenu de la liste : ")                   
            
            for i, element in enumerate(liste_de_course):   
                
                i += 1
                print(f"{i}. {element}")                
                
        else:
            print("Votre liste ne contient aucun éléments")
        continue            
        

    if reponse == "4":
        print("Nous allons vider la liste de course")
        liste_de_course.clear()
        save_liste_course.clear()
        continue

    if reponse == "5":        

        for i, element in enumerate(liste_de_course):

            if element in save_liste_course:                
                pass
            else:                        
                save_liste_course.append(element)
        
        with open("/home/vagrant/liste_de_course.json", "w") as f:
            json.dump(save_liste_course, f, indent=4)            

        print("Au revoir !!!")
        break
