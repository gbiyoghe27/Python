#Méthode1: Programme pour trouver le maximum de trois nombres

# Demande les trois nombres
#x = input("Entrez le premier nombre : ")
#y = input("Entrez le deuxième nombre : ")
#z = input("Entrez le troisième nombre : ")

# Convertit les trois nombres en entiers
#x = int(x)
#y = int(y)
#z = int(z)

# Initialise la variable max à la valeur du premier nombre
#max = x

# Compare les trois nombres
#if y > max:
    #max = y

#if z > max:
    #max = z

# Affiche le maximum
#print("Le maximum des trois nombres est", max)


#Methode 2: Programme pour trouver le maximum de trois nombres
#La troisième ligne utilise la fonction split() pour séparer la chaîne de caractères str en trois chaînes de caractères, une pour chaque nombre.

# Demande les trois nombres
x, y, z = input("Entrez trois nombres séparés par un espace : ").split()

# Convertit les trois nombres en entiers
x = int(x)
y = int(y)
z = int(z)

# Trouve le maximum
max = max(x, y, z)

# Affiche le maximum
print("Le maximum des trois nombres est", max)

#Methode3
# Demander à l'utilisateur de saisir trois nombres
#x = float(input("Veuillez saisir le premier nombre (x) : "))
#y = float(input("Veuillez saisir le deuxième nombre (y) : "))
#z = float(input("Veuillez saisir le troisième nombre (z) : "))

# Trouver le maximum entre x, y et z
#maximum = max(x, y, z)

# Afficher le résultat
#print("Le maximum entre", x, ",", y, "et", z, "est :", maximum)
