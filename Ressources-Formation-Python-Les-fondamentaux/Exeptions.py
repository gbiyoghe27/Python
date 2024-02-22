'''
Gerer les exeptions

try             tester un bloc de code
except          bloc execute en cas d'erreur
                except <NomExeption>:
                except Exception as err:
else            Executer si aucune exeption est levee
finally          Executer apres tous les blocs
'''

nb1 = input("Nombre 1 ? ")
nb2 = input("Nombre 2 ? ")

try:
    print(int(nb1)/int(nb2))
except Exception as err:
    print("erreur de type :", err)
else:
    print("L'operation s'est déroulee correctement")
finally:
    print("bloc finally")

print("fin de programme")


