
#On veut trouver les nombres positifs

liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

"""
#Cas 1 sans comprehension de liste



nombres_positifs = []

for i in liste:
    if i > 0:
        nombres_positifs.append(i)

print(nombres_positifs)

"""

"""
#Cas 2 avec compréhensions de liste

nombres_positifs = [i for i in liste if i > 0]
print(nombres_positifs)
"""
#Cas 2 multiplié les nombres positifs
nombres_positifs = [i * 2 for i in liste if i > 0]
print(nombres_positifs)