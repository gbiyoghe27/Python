'''
Scinder ou joindre une chaîne

methode :       split(<delimiteur) par defaut espace
                join(<liste>)
'''

prenoms = "luc,zoe,bob,marc,bil,jean"

liste =  prenoms.split(",")

chaine = " ".join(liste)

print(prenoms.partition("marc"))