"""
Louis Forget 405
 TP2
"""
import random

nb_aleatoire = random.randint(1, 100)
recommencer = True
nb_choisi = -1
nb_minimum = -1
nb_maximum = -1


def bornes():
    global nb_minimum, nb_maximum, nb_aleatoire

    nb_minimum = int(input("quel nombre desirez vous choisir comme le plus petit"))
    nb_maximum = int(input("quel nombre voulez vous choisir comme le plus grand"))
    nb_aleatoire = random.randint(nb_minimum, nb_maximum)


while recommencer:
    bornes()
    while nb_aleatoire != nb_choisi:

        nb_choisi = int(input(f"choisissez un nombre de {nb_minimum} a {nb_maximum}"))

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

