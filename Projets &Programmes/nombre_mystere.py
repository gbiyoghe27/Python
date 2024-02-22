# Importation de la fonction randint
from random import randint

# Définition du nombre mystère
nombre_mystere = randint(1, 100)

# Initialisation du nombre de coups
nb_coups = 0

# Boucle de jeu
while True:
    # Saisie du nombre par l'utilisateur
    try:
        nombre_saisi = int(input("Entrez un nombre entre 1 et 100 : "))
    except ValueError:
        print("Valeur invalide. Veuillez saisir un nombre entier.")
        continue

    # Vérification du nombre saisi
    if nombre_saisi < 1 or nombre_saisi > 100:
        print("Le nombre doit être compris entre 1 et 100.")
        continue

    # Incrémentation du nombre de coups
    nb_coups += 1

    # Comparaison du nombre saisi et du nombre mystère
    if nombre_saisi == nombre_mystere:
        print("Bravo ! Vous avez trouvé le nombre mystère en", nb_coups, "coups.")
        break
    elif nombre_saisi < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    else:
        print("Le nombre mystère est plus petit.")

# Choix de l'utilisateur
while True:
    choix = input("Voulez-vous rejouer ? (o/n) ")
    if choix.lower() in ("o", "n"):
        break

if choix == "o":
    print("Nouvelle partie...")
    # Relancement du programme
    main()
else:
    print("Au revoir !")
