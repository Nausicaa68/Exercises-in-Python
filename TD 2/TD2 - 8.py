x = int(input("Entrez x : "))
continuer = True
while continuer:
    continuer = False
    n = int(input("n : "))
    if n < 0:
        print("n doit etre positif")
        continuer = True

resultsomme = 0

for i in range(1,n+1):
    result = 1
    for j in range(i):
        result *= x   
        
    resultsomme += result

print("Somme de",x,"^i de i=1 à i=",n,"=",resultsomme)