from math import *
print("\t***Résolution d'une équation du second degré***")
continuer = True

while continuer:
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

    if a == 0:
        print("Cette équation n’est pas une équation du second degré")
    else:
        continuer = False

delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b-sqrt(delta))/(2*a)
    x2 = (-b+sqrt(delta))/(2*a)
    print("x1 =",x1)
    print("x2 =",x2)
if delta == 0:
    x1 = (-b)/(2*a)
    print("x =", x1)
if delta < 0:
    x1 = (-b)/(2*a)
    x2 = (sqrt(-delta))/(2*a)
    print("x1 =", x1," - i *", x2)
    print("x2 =", x1," + i *", x2)
    

    