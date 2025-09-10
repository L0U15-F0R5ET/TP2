import random

nb_aleatoire = random.randint(1, 100)

debut = input("bonjour, desirez vous commencer le jeu?")



if debut == "oui":
    nb_choisi = input("choisissez un nombre de 1 a 100")

    if nb_choisi < str(100):
        print("meilleure chance la prochaine fois")

    elif nb_choisi > str(100):
        print("meilleure chance la prochaine fois")

    else:
        print("bravo! desirez vous jouez une autre partie?")

else:
    print("au revoir")