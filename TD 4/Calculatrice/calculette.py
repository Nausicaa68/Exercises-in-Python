from operations import *

x1 = int(input("x1 : "))
x2 = int(input("x2 : "))

op = int(input("Opération :\n 1 - add\n 2 - sous\n 3 - mult\n 4 - div\n"))

if x2 == 0 and op == 4:
    print("erreur ! div par 0 impossible")
else:
    if op == 1:
        result = add(x1,x2)
    elif op == 2:
        result = sous(x1,x2)
    elif op == 3:
        result = mult(x1,x2)
    elif op == 4:
        result = div(x1,x2)
    print(result)