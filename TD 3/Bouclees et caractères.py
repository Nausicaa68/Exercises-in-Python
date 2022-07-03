"""for i in range(65,65+26):
    print(chr(i),"=",i,"en ASCII")
"""
a = input("Chaine : ")
voyelle = 0
voy = ""

for i in range(0,len(a)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i'or a[i] == 'o'or a[i] == 'u'or a[i] == 'y':
        voyelle += 1
        voy += a[i]
        
print("Il y a",voyelle,"voyelle(s).")
if voyelle != 0:
    print("Ce sont : ",voy)
    
