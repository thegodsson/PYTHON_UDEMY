import random

a = random.randint(0, 2)
b = random.randint(0, 2)




if b > a:
    print(f"Le nombre {b} est plus grand que le nombre {a}")
elif a < b:
    print(f"Le nombre {a} est plus petit que le nombre {b}")

else:
    print(f"Le nombre {a} et le nombre {b} sont égaux")




