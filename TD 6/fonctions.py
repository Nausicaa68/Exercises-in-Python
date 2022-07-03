def nb_voyelles(chaine, taille):
    liste_voyelle = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
    compteur = 0
    
    if taille>0:
        i = chaine[taille-1]
        if ord(i) in liste_voyelle:
            compteur += 1
        compteur = compteur + nb_voyelles(chaine, taille-1)
    return compteur

def palindr_recurs(chaine):
    taille = len(chaine)
    if taille == 0 or taille == 1:
        return True
    else:
        if chaine[0] == chaine[taille-1]:
            return palindr_recurs(chaine[1:taille-1])
        else:
            return False

def copi(chaine, debut):
    taille = len(chaine)
    chaine2 = ""
    if debut < taille :
        chaine2 += chaine[debut]
        chaine2 += copie(chaine, debut+1)
    
    return chaine2

