a = int(input("a ? "))
b = int(input("b ? "))
c = int(input("c ? "))

if a>b and a>c:
    maxi = a
if b>a and b>c:
    maxi = b
if c>a and c>b:
    maxi = c
else:
    print("il n'y a pas de maximum")
    test = 1
    
if test != 1:
    print(maxi, "est le maximum entre", a, ",",b,"et",c)