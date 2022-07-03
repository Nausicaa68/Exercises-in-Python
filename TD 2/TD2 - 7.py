x = int(input("Entrez x : "))
n = int(input("Entrez l'exposant : "))
result = 1

for i in range(abs(n)):
    result *= x

if n>0:
    print(x,"^",n,"=",result)
if n<0:
    print(x,"^",n,"= 1 /",result,"~",1/result)
    
