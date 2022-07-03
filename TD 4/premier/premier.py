from fonction import *

a = -1
while a < 0:
    a = int(input("a : "))

if prem(a) == True:
    print("ce nombre est premier")
else:
    print("ce nombre n est pas premier")