def inverse(chaine):
    chaine_reverse = ""
    for i in range(len(chaine)-1, -1, -1):
        chaine_reverse += chaine[i]
    
    return chaine_reverse

def maj_min(chaine):
    minuscule = 0
    majuscule = 0
    
    for i in range(len(chaine)):
        caract = chaine[i]
        if 97<=ord(caract)<=122:
            minuscule += 1
        if 65<=ord(caract)<=90:
            majuscule += 1
            
    return minuscule, majuscule

def voyelles(chaine):
    nb_voy = 0
    voyelles = [65, 97, 69, 101, 73, 105, 79, 111, 85, 117, 89, 121]
    
    for i in range(len(chaine)):
        caract = chaine[i]
        if ord(caract) in voyelles:
            nb_voy += 1
            
    return nb_voy

def palind(chaine):
    palindrome = False
    chaine = chaine.upper()
    
    for i in range(len(chaine)):
        if chaine[i] == chaine[len(chaine)-1-i]:
            palindrome = True
        else:
            palindrome = False
            
    return palindrome

def pang(chaine):
    pangramme = False
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range(len(chaine)):
        if chaine[i] in alphabet:
            alphabet.remove(chaine[i])
            if 65<=ord(chaine[i])<=90:
                caract = chr(ord(chaine[i])+32)
            else:
                caract = chr(ord(chaine[i])-32)
            
            alphabet.remove(caract)
                
    
    if alphabet == []:
        pangramme = True
        
    return pangramme

