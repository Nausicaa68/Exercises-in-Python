from Fonctions import maj_min

chaine = input("chaine : ")

minuscule = maj_min(chaine)[0]
print("Nb of minuscule :",minuscule)
majuscule = maj_min(chaine)[1]
print("Nb of majuscule :",majuscule)
