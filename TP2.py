import random

nb_aleatoire = random.randint(1, 100)

nb_choisi = -1

while nb_aleatoire != nb_choisi:

    nb_choisi = input("choisissez un nombre de 1 a 100")

    if nb_choisi < str(100):
        print("meilleure chance la prochaine fois")

    elif nb_choisi > str(100):
        print("meilleure chance la prochaine fois")

    else:
        continu=input("bravo!")
fin = input("desirez vous jouez une autre partie?")
