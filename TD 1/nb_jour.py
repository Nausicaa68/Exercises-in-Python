nb_jour = int(input("Nombre de jour : "))

annee = int(nb_jour / 365)
print(annee)
nb_jour -= annee*365

semaine = int(nb_jour/7)
print(semaine)
nb_jour -= semaine*7

print(nb_jour)