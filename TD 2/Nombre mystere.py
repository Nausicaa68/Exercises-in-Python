from random import randint

print("Bienvenue ! Trouvez le nombre mystère. Il est compris entre 1 et 10000")
nb_mystere = randint(1,10000)

nb_choix = input("Entrer votre choix : ")
nb_choix = int(nb_choix)
compteur = 1

while (nb_mystere != nb_choix) and (compteur < 10):
    if nb_mystere > nb_choix:
        print("Plus grand")
    if nb_mystere < nb_choix:
        print("Plus petit")
    if nb_mystere == nb_choix:
        print("Et c'est gagné !")

    nb_choix = input("Entrer votre choix : ")
    nb_choix = int(nb_choix)
    compteur += 1

if compteur == 10:
    print("Perdu ! Vous avez utilisé vos 10 coups. Le nombre mystère était", nb_mystere)
else:    
    print("Bravo ! Vous avez trouvé le nombre mystère en", compteur,"coups\n\t********* FELICITATIONS *********\n")