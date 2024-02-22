'''
Structure de donnée Dictionnaire
mots--->definition

dico = {<key>:<valeur> , <key2>:<valeur>}

modifier/ajouter une valeur      dico["prenom"]= "luc"
supprimer une paire              pop()  
effacer le dictionnaire          clear()  
copier un dictionnaire           copy()  

for val in dico.values():
for k in dico.keys():
for k,v in dico.items():
'''

dico = {"nom":"parein" , "prenom":"jean" , "age":47}

if "taille" in dico:
    print("la cle age est presente")
else:
    print("non present")