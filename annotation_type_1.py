
def add(a, b):
    return a + b

add("10" + 1)

#print(add)


def add2(a: int = 0, b: int = 0) -> int:
    return a + b

resultat = add2("12" + 2)
print(resultat)


