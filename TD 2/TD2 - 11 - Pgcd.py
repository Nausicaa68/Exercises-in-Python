a = int(input("a : "))
b = int(input("b : "))
if a<0 or b<0:
    print("Erreur ! a et/ou b doit/doivent être positif(s)")

while a!= b:
    if a>b:
        a = a-b
    if a<b:
        b = b-a
    if a == b:
        pgcd = a

if a == b:
    pgcd = a

print(pgcd)