

d = {

    "prenom": "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}

"""
for cle in d:
    #print(cle)
    print(d[cle])
"""

for valeur in d.values():
    print(valeur)

print("------------")

for cle in d:
    print(cle)

print("------------")

for cle in d.keys():
    print(cle)

print("------------")

for cle, valeur in d.items():
    print(f"Les cles : {cle}")
    print(f"Leurs valeurs : {valeur}")

