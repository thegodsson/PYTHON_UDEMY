

#exemple de comphension de liste : nombres_positifs = [i * 2 for i in liste if i > 0]



#Sans comphéension

#Exo 1
#nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
#Exo 2
#nombres = range(-10, 10)
#Exo 3
#nombres = range(5)

"""
#Exo 1
nombres_pairs = []

for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

print(nombres_pairs)
"""


#Exo 1 Avec comphéension

"""
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)
"""

"""
#Exo 2
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)
"""

"""
#Exo 3

nombres_doubles = [i * 2 for i in nombres]
print(nombres_doubles)
"""


#Exo 4



