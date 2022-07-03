wo = 2
xo = -1
p = int(input("Vous voulez calculer U combien : "))

for i in range(0,p):
    w = wo + xo
    x = xo - wo
    wo = w
    xo = x
print("wn =",w)
print("xn =",x)