

liste_de_course = []

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
        else:
            print(f"L'article {retirer} n'est pas dans la liste")
       
        continue

    if reponse == "3":        
        if len(liste_de_course) > 0:   
            print("Voici le contenu de la liste : ")                   
            #for i in range(len(liste_de_course)):
            for i, element in enumerate(liste_de_course):
                #y = 1
                #y += i                
                #print(f"{y}. {liste_de_course[i]}")
                i += 1
                print(f"{i}. {element}")
        else:
            print("Votre liste ne contient aucun éléments")
        continue            
        

    if reponse == "4":
        print("Nous allons vider la liste de course")
        liste_de_course.clear()
        continue

    if reponse == "5":
        print("Au revoir !!!")
        break
