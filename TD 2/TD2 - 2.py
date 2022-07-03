total = 0
compteur = 0
continuer = True

while continuer: 
    nombre = input("\nPour arreter, taper @ \nRentrez un nombre : ")
    if nombre == "@":
        continuer = False
    else:
        nombre = int(nombre)
        total += nombre
        compteur += 1

if compteur == 0:
    print("Calcul impossible")
else: 
    moyenne = int(total/compteur)
    print("La moyenne est :", moyenne)