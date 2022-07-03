compteur = 0
continuer = True

while continuer: 
    nombre = input("\nPour arreter, taper @ \nRentrez un nombre : ")
    if nombre == "@":
        continuer = False
    else:
        nombre = int(nombre)
        if compteur == 0:
            minimum = nombre
        elif minimum > nombre:
            minimum = nombre
        compteur += 1
if compteur == 0:
    print("Calcul impossible")
else:
    print("Le minimum est", minimum)