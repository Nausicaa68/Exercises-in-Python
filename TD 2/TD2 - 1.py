repeter = True

while repeter:
    message = input("Entrez un message : ")
    nb = int(input("Entrez un nombre : "))     
    if nb < 0:
        print("Votre nombre est négatif")
    else:
        repeter = False
i = 0
while i < nb:
    print(message)
    i += 1
    