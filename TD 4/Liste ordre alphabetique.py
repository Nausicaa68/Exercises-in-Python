chaine = "green-red-yellow-black-white"
liste = ['green', 'red', 'yellow', 'black', 'white']

liste_somme = []

def ordre_alph(liste):
    for i in range(len(liste)):
        mot = liste[i]
        for j in range(len(mot)):
            chiffre = ord(mot[j])*(10**(i+1))
            somme += chiffre
        
        liste_somme.append(somme)
        
    print(liste_somme)