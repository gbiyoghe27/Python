# Import de la bibliotheque random
import random

# Affichage du titre
titre = "Nombre mystere (1/100)"
print("*"*len(titre))
print(titre)
print("*"*len(titre))

# Nombre aleatoire
nb = random.randint(1,100)

# Nombre de coup
c=1

# Rejouer
replay = True

while replay:

    # Boucle de jeu
    while True:
        n = input(f"(Tentative(s):{c} - votre nombre ? ")

        try:
            n=int(n)
            if n<1 or n>100:
                print("Vous devez renseigner un nombre entre 1 et 100")
                continue
        except:
            print("Vous devez renseigner un nombre entier...")
            continue

        # Incrementation du compteur
        c+=1

        # Test du nombre mystere
        if n==nb:
            print(f"Bravo, vous avez trouve le nombre mystere {nb}")
            print(f"Nombre de tentative(s): {c-1}")
            break
        elif n<nb:
            print("Non, c'est plus grand...")
        else:
            print("Non, c'est plus petit...")

    # Rejouer
    rep = input("Voulez vous rejouer (O/N) ?")

    if rep.upper()=="N":
        replay = False
    else:
        print("")
        # Nombre aleatoire
        nb = random.randint(1,100)
        # Nombre de coup
        c=1

