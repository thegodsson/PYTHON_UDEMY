

liste = ["1", "4", "25", "Paul", "3", "Pierre"]


#Cas continue

for element in liste:
    if element.isdigit():
        continue
    print(element)

#cas break
"""
for element in liste:
    if element.isdigit():
        break
    print(element)
"""