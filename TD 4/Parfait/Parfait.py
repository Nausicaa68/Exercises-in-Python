from Fonctions import parfait

a = -1
while a < 0:
    a = int(input("a : "))

if parfait(a) == 1:
    print("ce nombre parfait")
else:
    print("ce nombre n est pas parfait")