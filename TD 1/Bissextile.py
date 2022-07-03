annee = int(input("Saisissez une année : "))

if annee%400 == 0 or (annee%4 == 0 and annee%100 != 0):
    print("L'année",annee,"est bissextile")
else:
    print("L'année",annee,"n'est pas bissextile")