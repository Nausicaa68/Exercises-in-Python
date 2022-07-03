#ex1
def dico_carre(n):
    dico = {}
    for i in range(1,n+1):
        dico[i] = i*i
    return dico

n = 5
dicoCarre = dico_carre(n)
print(dico_carre)

#ex2
def dico_itere(dico):
    chaine = ""
    for valeur in dico.values():
        chaine += str(valeur) + " "
        
    return chaine

dicoItere = dico_itere(dicoCarre)
print(dicoItere)

#ex3
def dico_add_mult(dico):
    somme = 0
    mult = 1
    
    for valeur in dico.values():
        somme += valeur
        mult *= valeur
        
    return somme, mult

somme = dico_add_mult(dicoCarre)[0]
multip = dico_add_mult(dicoCarre)[1]
print(somme)
print(multip)

#ex4
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

def dico_combin(dico1, dico2):
    dico3 = {}
    
    for cle1 in dico1.keys():
        for cle2 in dico2.keys():
            if cle1 == cle2:
                dico3[cle2] = dico1[cle1] + dico2[cle2]
            
    for cle3 in dico1.keys():
        if cle3 not in dico3:
            dico3[cle3] = dico1[cle3]
            
    for cle3 in dico2.keys():
        if cle3 not in dico3:
            dico3[cle3] = dico2[cle3]
                
    return dico3

d3 = dico_combin(d1, d2)
print(d3)

#ex5
dico = ['the', 'cat', 'sat', 'on', 'the', 'mat']

def compter_les_mots(dico):
    dico2 = {}
    
    for cle in dico:
        if cle not in dico2:
            dico2[cle] = 1
        else:
            dico2[cle] += 1
    return dico2

print(compter_les_mots(dico))