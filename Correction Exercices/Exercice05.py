#Méthode1

# Demander à l'utilisateur de saisir un nombre entier
#nombre = int(input("Veuillez saisir un nombre entier : "))

# Vérifier si le nombre est pair ou impair
#if nombre % 2 == 0:
   # print(nombre, "est un nombre pair.")
#else:
    #print(nombre, "est un nombre impair.")

    #Méthode2

    # Programme pour déterminer si un nombre est pair ou impair
    #La quatrième ligne utilise l'opérateur modulo (%) pour vérifier si le nombre est divisible par 2.
    # Si le reste de la division est égal à 0, alors le nombre est pair. Sinon, le nombre est impair.

# Demande le nombre à l'utilisateur
nombre = input("Entrez un nombre entier : ")

# Convertit le nombre en entier
nombre = int(nombre)

# Vérifie si le nombre est divisible par 2
if nombre % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")

