# Méthode 1: Programme pour calculer la somme 1 + 2 + ... + n

# Demande le nombre n
#n = input("Entrez un nombre entier n : ")

# Convertit le nombre n en entier
#n = int(n)

# Calcule la somme
#somme = n * (n + 1) // 2

# Affiche la somme
#print("La somme 1 + 2 + ... + n est", somme)


# Methode 2:Programme pour calculer la somme 1 + 2 + ... + n

# Demande le nombre n
n = input("Entrez un nombre entier n : ")

# Convertit le nombre n en entier
n = int(n)

# Initialise la variable somme à 0
somme = 0

# Calcule la somme
for i in range(1, n + 1):
    somme += i

# Affiche la somme
print("La somme 1 + 2 + ... + n est", somme)
