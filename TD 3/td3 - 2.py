liste = [85,2,36,8,5,4,64,52]
minimum = liste[0]

for i in range(0,len(liste)):
    if minimum > liste[i]:
        minimum = liste[i]
        
print("min :", minimum)