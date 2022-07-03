def tableau_2D(tab, lg, cl):
    tableau = []
    ligne = []
    h = 0
    for i in range(lg):
        for j in range(cl):
            ligne.append(tab[h])
            h += 1
        
        tableau.append(ligne)
        ligne = []
    
    return tableau

tab = []
lignes = int(input("Nb de lignes : "))
colonnes = int(input("Nb de colonnes : "))

nb_valeur = lignes*colonnes

for i in range(nb_valeur):
    a = int(input("Valeur : "))
    tab.append(a)

print(tableau_2D(tab, lignes, colonnes))
