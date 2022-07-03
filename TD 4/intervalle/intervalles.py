from fonction import *
maxi = int(input("maxi : "))
mini = int(input("mini : "))
x = int(input("x : "))

if intervalle(mini,maxi,x) == 1:
    print(x, "appartient à l'intervalle [",mini,";",maxi,"]")
if intervalle(mini,maxi,x) == 0:
    print(x, "n'appartient pas à l'intervalle [",mini,";",maxi,"]")