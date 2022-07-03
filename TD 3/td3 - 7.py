liste = [5,8,56,75,85,105,256,5]
mini = 0
ordonnee = True

for i in range(1,len(liste)):
    mini = liste[i-1]
    
    if liste[i] < mini:
        print("La liste n'est pas ordonnée")
        ordonnee = False
        
if ordonnee == True:
    print("La liste est ordonnée")