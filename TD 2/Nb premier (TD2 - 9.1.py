nb = int(input("Nombre : "))
compteur = 2
premier = True

while compteur < nb:
    if nb/compteur == int(nb/compteur):
        print("le nombre n'est pas premier")
        premier = False
        break
    compteur += 1

if premier == True:
    print("Le nombre est premier")
