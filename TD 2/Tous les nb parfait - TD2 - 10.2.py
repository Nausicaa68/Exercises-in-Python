for nombre in range(1,1000):
    somme = 0
    for i in range(1,nombre):
        if nombre % i == 0:
            somme = somme + i
    if somme == nombre:
        print(nombre)
