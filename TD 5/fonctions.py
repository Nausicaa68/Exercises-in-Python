def afficher_nb_cr(n):
    if n > 0:
       afficher_nb_cr(n-1)
       print(n)
       
def afficher_nb_decr(n):
    if n > 0:
       print(n)
       afficher_nb_decr(n-1)

def triangle(n):
    if n>0:
        triangle(n-1)
        chaine = n*"*"
        print(chaine)
        
def triangle_inv(n):
    if n>0:
        chaine = n*"*"
        print(chaine)
        triangle_inv(n-1)
        
def pyra_inv(n, taille):
    if n>0:
        chaine = (taille-n)*" " + (n-1)*"*-" + "*"
        print(chaine)
        pyra_inv(n-1, taille)

def pyra(n, taille):
    if n>0:
        pyra(n-1, taille)
        chaine = (taille-n)*" " + (n-1)*"*-" + "*"
        print(chaine)
        
def reverse(chaine, chaine2, i):
    if i>-1:
        chaine2 += chaine[i]
        if i == 0:
            print(chaine2)

        reverse(chaine, chaine2, i-1)

