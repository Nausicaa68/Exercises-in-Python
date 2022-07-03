liste = [85,2,36,8,5,4,64,52,5]
valeur = 4
continuer = True

for i in range(0,len(liste)):
    if liste[i] == valeur and continuer == True:
        print(valeur,"est dans la liste, à la position", i+1)
        continuer = False
if continuer == True:
    print(valeur,"n'est pas dans la liste")