liste = [85,2,36,8,5,4,64,52,5]
valeur = 5

compteur = 0
for i in range(0,len(liste)):
    if liste[i] == valeur:
        compteur += 1
if compteur != 0:
    print(valeur,"est", compteur,"fois dans la liste.")
else:
    print(valeur,"n'est pas dans la liste.")