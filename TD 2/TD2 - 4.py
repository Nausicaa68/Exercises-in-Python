chaine = ""
for i in range(2000,3200):
    if (i%7 == 0) and (i%5 != 0):
        i = str(i)
        chaine += i+";"
print(chaine)