# Programme pour demander deux nombres à l'utilisateur et afficher leur maximum

# Demande les deux nombres
a, b = input("Entrez deux nombres séparés par un espace : ").split()

# Convertit les deux nombres en entiers
a =int(a)
b = int(b)

# Trouve le maximum des deux nombres
max = max(a, b)

# Affiche le maximum
print("Le maximum des deux nombres est", max)
