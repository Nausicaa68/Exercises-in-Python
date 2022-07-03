#ex3
def diagonale(tab):
    chaine =""
    
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i == j:
                chaine += str(tab[i][j])
            else:
                chaine += " "
        print(chaine)
        chaine = ""
        
tableau = [[1,2,3],[4,5,6],[7,8,9]]
diagonale(tableau)

def diag(tab):
    chaine =""
    
    for i in range(len(tab)):
        for j in range(len(tab)):
            if i+j == len(tab)-1:
                chaine += str(tab[i][j])
            else:
                chaine += " "
        print(chaine)
        chaine = ""

tableau = [[1,2,3],[4,5,6],[7,8,9]]
diag(tableau)