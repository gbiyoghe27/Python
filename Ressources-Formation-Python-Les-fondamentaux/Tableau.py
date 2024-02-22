'''
Structure de donnée : Liste

Multi-dimension

"nom"           "prenom"        "film"
Stallone        Sylvester       Rocky
Swartzeneger    Arnold          Predator

'''

tab = [
    ["Stallone", "Sylvester", ["rocky", "cobra"]], #0
    ["Swartzeneger", "Arnold", "Predator"], #1
    ["Gibson", "Mel", "Braveheart"] #2
]

print(tab[0][2][1])

print(type(tab))
