def aff_tab_2D(tab2D):
    chaine = ""
    taille = len(tab2D)
    
    for i in range(taille):
        for j in range(taille):
            chaine += str(tab2D[i][j])
        print(chaine)   #on met un print dans cette fonction car elle ne sert qu'à afficher le plateau. Autant mettre le print là
        chaine = ""
    print("")
    
tab = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aff_tab_2D(tab)