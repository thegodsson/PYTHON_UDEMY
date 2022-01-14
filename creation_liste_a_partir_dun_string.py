
"""
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses.split(", ") # --> Pas correct la chaine de caractère ne vas pas se transformé en liste
print(courses)

courses = courses.split(", ")  # --> Correct , la chaine de caractère vas se transformé en liste
print(courses)
"""

#On pourrait donc différencier la liste de la chaine de caractère:

courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses_liste = courses.split(", ")

print(courses)
print(courses_liste)

#Si le caractère sur lequel on split n'existe pas, une liste sera quan même créé , mais avec un seul élément exemple:
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses = courses.split("|")

print(courses)




