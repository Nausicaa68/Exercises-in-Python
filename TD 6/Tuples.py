"""
#ex1
def user():
    prenom = input("Prenom ? ")
    nom = input("Nom ? ")
    age = int(input("Age ? "))
    
    return prenom, nom, age

tupl = user()
print(tupl)

#ex2
def tuple_string(tupl):
    chaine = ""
    for i in range(len(tupl)):
        chaine += str(tupl[i]) + " "
    return chaine

chaine = tuple_string(tupl)
print(chaine)

#ex3
tupl = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def quatriemes_elements(tupl):
    return tupl[3], tupl[len(tupl)-4]
print(quatriemes_elements(tupl))

#ex4
def separation(chaine):
    nbr = ""
    liste = []
    
    for i in range(len(chaine)):
        if chaine[i] == ",":
            nbr = int(nbr)
            liste.append(nbr)
            nbr = ""
        else:
            nbr += chaine[i]
    return liste, tuple(liste)

chaine = "1,2,3,4,5,6,7,8,9,10"
print(separation(chaine)[0])
print(separation(chaine)[1])
"""
#ex5
def mini(a, b):
    if a<b:
        return a
    elif b>a:
        return b
    else:
        return a


def trie(liste):
    
    modif = 1 
    for k in range(2, 0, -1):
        while modif == 1:
            modif = 0
            for i in range(1,len(liste)):
                j = 0
                if liste[i-1][k] > liste[i][k]:
                    a = liste[i-1]
                    b = liste[i]
            
                    liste[i] = a
                    liste[i-1] = b
                
                    modif = 1


    for i in range(1,len(liste)):
        taille1 = len(liste[i-1][0])
        taille2 = len(liste[i][0])
        minimum = mini(taille1, taille2)
        
        continuer = True
        j = 0
        while continuer and j<minimum:
            if ord(liste[i-1][0][j]) > ord(liste[i][0][j]):
                a = liste[i-1]
                b = liste[i]
                
                liste[i] = a
                liste[i-1] = b
                
                continuer = False
            j += 1
    
    return liste
      
liste = [('Tom','19', '80'), ('John', '20', '90'), ('John', '22', '90'), ('John', '20', '98')]
print(liste)
liste2 = trie(liste)
print(liste2)