import random

nb_aleatoire = random.randint(1, 100)

recommencer = True


nb_choisi = -1

while recommencer:
    while nb_aleatoire != nb_choisi:

        nb_choisi = int(input("choisissez un nombre de 1 a 100"))

        if nb_choisi < nb_aleatoire:
            print("meilleure chance la prochaine fois, chiffre trop petit")

        else:
            print("meilleure chance la prochaine fois, chiffre trop grand")

    print("Bien joué!")
    finale = input("desirez vous jouez une autre partie?y/n")
    if finale == "y":
        print("ok")
        nb_choisi = 1
        nb_aleatoire = random.randint(1, 100)
    elif finale == "n":
        recommencer = False

print("a la prochaine")