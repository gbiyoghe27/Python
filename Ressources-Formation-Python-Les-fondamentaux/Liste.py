'''
Structure de données : Liste
len(liste)      total d'elements dans la liste

append      Ajouter un element a la fin de la liste
insert      Ajouter un element selon un index
remove      Supprimer un element par sa valeur
pop         Supprimer un element par son index
index       Afficher l'index selon une valeur
count       Nombre d'elements qui apparrait
sort        Trier une liste par ordre croissant
reverse     Inverser l'ordre
copy        Copie d'une liste
extend      Etendre une liste
clear       Effacer une liste
'''


ma_liste = ["zebra", "zoe","rouge", "alain"]

ma_liste.clear()

ma_liste = [100,110,120]

index = 0
for element in ma_liste:
    print(index,element)
    index+=1