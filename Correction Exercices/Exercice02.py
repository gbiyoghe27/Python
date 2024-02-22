
#Methode1
# Programme pour demander deux nombres à l'utilisateur et afficher leur somme

# Demande le premier nombre
#a = input("Entrez le premier nombre : ")

# Convertit le premier nombre en entier
#a = int(a)

# Demande le deuxième nombre
#b = input("Entrez le deuxième nombre : ")

# Convertit le deuxième nombre en entier
#b = int(b)

# Calcule la somme des deux nombres
#somme = a + b

# Affiche la somme
#print("La somme des deux nombres est", somme)


#Methode2
# Programme pour demander deux nombres à l'utilisateur et afficher leur somme

# Demande les deux nombres en une seule fois
a, b = input("Entrez deux nombres séparés par un espace : ").split()

# Convertit les deux nombres en entiers
a = int(a)
b = int(b)

# Calcule la somme des deux nombres
somme = a + b

# Affiche la somme
print("La somme des deux nombres est", somme)
