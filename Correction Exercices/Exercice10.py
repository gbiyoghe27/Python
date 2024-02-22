# Methode 1 :Programme pour calculer la surface et le périmètre d'un cercle

# Demande le rayon du cercle
rayon = input("Entrez le rayon du cercle : ")

# Convertit le rayon en nombre réel
rayon = float(rayon)

# Calcule la surface
#cette ligne est importante car elle permet d'importer les ressources de formules mathématiques
import math
surface = math.pi * rayon ** 2

# Calcule le périmètre
import math
#cette ligne est importante car elle permet d'importer les ressources de formules mathématiques
perimetre = 2 * math.pi * rayon

# Affiche la surface et le périmètre
print("La surface du cercle est", surface)
print("Le périmètre du cercle est", perimetre)

#methode2:
import math

# Demander à l'utilisateur de saisir le rayon du cercle
rayon = float(input("Veuillez saisir le rayon du cercle : "))

# Calculer la surface du cercle
surface = math.pi * (rayon ** 2)

# Calculer le périmètre du cercle
perimetre = 2 * math.pi * rayon

# Afficher les résultats
print("La surface du cercle est :", surface)
print("Le périmètre du cercle est :", perimetre)

