multiplie = int(input("Entrez le multipliée : "))
multipliant = int(input("Entrez le multipliant : "))


moins = False

if (multipliant < 0 and multiplie > 0)or(multipliant > 0 and multiplie < 0):
    moins = True

multiplie = abs(multiplie)
multipliant = abs(multipliant)

resultat = 0
for i in range(multipliant):
    resultat += multiplie
    
if moins:
    print("-",resultat)
else:
    print(resultat)