"""
#Il suffit qu'un seul booléen soit vrai pour que cela nous retourne vrai
print(any([False, False, True, False]))
"""

"""
#Il faudrait que tout les éléments soit vrai pour qu'il nous retourne vrai, ce n'est pas le cas donc se sera faux
print(all([False, False, True, False]))
"""

#Ces fonctions sont généralement avec des comphésensions de liste:
#exemple:

all([f.endswith(".jpg") for f in files])

notes = [12, 14, 20, 10, 8]

any([x > 18 for x in notes])
