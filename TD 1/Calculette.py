continuer = True

while continuer:
    
    x = int(input("x : "))
    y = int(input("y : "))
    print("Quelle opération voulez-vous faire ?")
    print("1 - Multiplication")
    print("2 - Division")
    print("3 - Addition")
    print("4 - Soustraction")
    print("99 - Quitter")
    choix = int(input("Votre choix : "))

    if choix == 1:
        print(x,"*",y,"=",x*y)
    if choix == 2 and y != 0:
        print(x,"/",y,"=",x/y)
    if choix == 2 and y == 0:
        print("Erreur ! Division par 0 impossible !")
    if choix == 3:
        print(x,"+",y,"=",x+y)
    if choix == 4:
        print(x,"-",y,"=",x-y)
    if choix == 99:
        continuer = False
        
print("Bye")
