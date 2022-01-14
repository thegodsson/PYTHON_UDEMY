def affiche(message):  #message est un paramètre
    print(message)

affiche("Bonjour") #Bonjour est un argument

#On peut définir des valeur par default pour un paramètre

def affiche2(message="Message par défault"):
    print(message)

affiche2()
affiche2("Autre test")


#Autre exemple, python mettra par defaut a=10 , b=5

def addition(a, b):
    return a + b

print(addition(10, 5))

#Cependant on peut indiqué à python la valeur à prendre

def addition2(a, b):
    return a + b

print(addition2(b=10, a=5))


def add(a=1, b=2, c=3):
    return a + b

print(add(c=5, b=6))