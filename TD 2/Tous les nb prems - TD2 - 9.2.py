nb = 1
while nb<1000:
    compteur = 2
    premier = True

    while compteur < nb:
        if nb/compteur == int(nb/compteur):
            premier = False
            break
        compteur += 1

    if premier == True:
        print(nb)
    
    nb += 1