# Methode1 Programme pour calculer n!

# Demande le nombre n
n = input("Entrez un nombre entier n : ")

# Convertit le nombre n en entier
n = int(n)

# Initialise la variable n! à 1
n_factorielle = 1

# Calcule n!

for i in range(1, n + 1):
    n_factorielle *= i

# Affiche n!
print("n! est", n_factorielle)


# Methode2 Programme pour calculer n!

# Demande le nombre n
n = input("Entrez un nombre entier n : ")

# Convertit le nombre n en entier
n = int(n)

# Initialise la variable n! à 1
n_factorielle = 1

# Calcule n!
#La cinquième ligne utilise une boucle for pour calculer n!. La boucle commence à 1 et s'arrête à n. À chaque itération, la valeur de n_factorielle est multipliée par i.
for i in range(1, n + 1):
    n_factorielle *= i

# Affiche n!
print("n! est", n_factorielle)
