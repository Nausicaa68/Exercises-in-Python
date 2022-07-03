liste = [5,8,56,75,85,105,256]
liste2 = []
valeur = 300
mettre = True 

for i in range(0,len(liste)):    
    if valeur < liste[i] and mettre == True:
        liste2.append(valeur)
        mettre = False
        
    liste2.append(liste[i])

if mettre == True:
    liste2.append(valeur)

print(liste2)