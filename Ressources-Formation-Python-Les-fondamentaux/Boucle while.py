'''
Boucle while---> tant que
'''
while True:
    com = input("com>")
    
    if com == "hello":
        print("Salut a toi !!!!")
    elif com == "stop":
        break
    else:
        print("Commande non valide")

    