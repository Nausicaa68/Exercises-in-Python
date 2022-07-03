def parfait(nombre):
    somme = 0
    
    for i in range(1,nombre):
        if nombre % i == 0:
            somme += i

    if somme == nombre:
        return 1
    else:
        return 0