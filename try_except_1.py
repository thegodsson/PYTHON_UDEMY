a = 5
b = 2

"""
try:
    print(a / b)
except:
    print("Division par zéro impossible")
"""

#Ce qui est plus haut est trop vaste si je remplace la valeur de bas par un strin exemple "Bonjour", ce n'est plus une ZeroDivisionError

#Pour cela il faut être plus précis dans le except

try:
    resultat = a / b
except ZeroDivisionError:
    print("Division par zéro impossible")

except TypeError:
    print("La variable b n'est pas du bon type")
except NameError as e:
    print("Erreur: ", e)
else:
    print(resultat)
finally:
    print("Fin du bloc")