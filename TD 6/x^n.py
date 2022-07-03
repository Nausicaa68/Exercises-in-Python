def puissance(x, n):
    if n == 1:
        resultat = x
    if n > 1:
        resultat = x* puissance(x, n-1)
    return resultat
    
x = 4
n = 3
print(puissance(x, n))