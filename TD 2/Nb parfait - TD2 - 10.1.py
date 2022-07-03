r = True
while r:
    nombre = int(input("Entrez un nombre : "))
    if nombre < 0 :
        print("Rentrer un nombre positif")
        r = True
    else:
        r = False

somme = 0

for i in range(1,nombre):
    if nombre % i == 0:
        somme += i

if somme == nombre:
    print(nombre,"est parfait.")
else:
    print(nombre,"n'est pas parfait.")