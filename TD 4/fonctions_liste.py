def carre(): 
    liste_carre = []
    for i in range(1,30+1):
        liste_carre.append(i*i)
    
    return liste_carre

def somme_liste(liste):
    somme = 0
    for i in range(len(liste)):
        somme += liste[i]
    return somme

def comparer(liste, n):
    erreur = "La valeur n'est pas dans la liste"
    for i in range(len(liste)):
        if liste[i] == n:
            erreur = i+1  #de tel sorte à ce qu'il retourne la position dans la liste d un point de vue humain
            break
    return erreur

def minimum(liste):
    mini = liste[0]
    for i in range(1, len(liste)):
        if mini >= liste[i]:
            mini = liste[i]
            
    return mini

def sans_doublons(liste):
    new_liste = []
    re_liste = []
    for i in range(len(liste)):
        if (liste[i] in new_liste) == False:
            new_liste.append(liste[i])
    
    for i in range(len(new_liste)):
        mini = minimum(new_liste)
        re_liste.append(mini)
        new_liste.remove(mini)

    return re_liste

def parite(liste):
    liste_pair = []
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            liste_pair.append(liste[i])
    return liste_pair

