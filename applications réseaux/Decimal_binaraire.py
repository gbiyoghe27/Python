def convertir_decimal_binaire(nombre_decimal):
  """
  Fonction pour convertir un nombre décimal en binaire.

  Args:
    nombre_decimal: Le nombre décimal à convertir.

  Returns:
    Une chaîne de caractères représentant le nombre binaire.
  """

  if nombre_decimal < 0:
    return f"-{convertir_decimal_binaire(-nombre_decimal)}"
  reste = abs(nombre_decimal)
  binaire = ""
  while reste > 0:
    reste, quotient = reste // 2, reste % 2
    binaire = str(quotient) + binaire
  return binaire

def convertir_binaire_decimal(nombre_binaire):
  """
  Fonction pour convertir un nombre binaire en décimal.

  Args:
    nombre_binaire: La chaîne de caractères représentant le nombre binaire.

  Returns:
    Le nombre décimal correspondant.
  """

  if nombre_binaire[0] == "-":
    return -convertir_binaire_decimal(nombre_binaire[1:])
  nombre_decimal = 0
  puissance = 1
  for chiffre in nombre_binaire[::-1]:
    nombre_decimal += int(chiffre) * puissance
    puissance *= 2
  return nombre_decimal

def main():
  """
  Fonction principale de l'application.
  """

  while True:
    choix = input("Choisissez une conversion (décimal/binaire): ").lower()
    if choix not in ("decimal", "binaire"):
      print("Choix invalide.")
      continue

    valeur = input("Entrez la valeur à convertir: ")

    try:
      if choix == "d":
        nombre_decimal = int(valeur)
        resultat_binaire = convertir_decimal_binaire(nombre_decimal)
        print(f"{nombre_decimal} en binaire est : {resultat_binaire}")
      else:
        nombre_binaire = valeur
        resultat_decimal = convertir_binaire_decimal(nombre_binaire)
        print(f"{nombre_binaire} en décimal est : {resultat_decimal}")
    except ValueError:
      print("Valeur invalide.")

    continuer = input("Voulez-vous continuer (y/n) ? ").lower()
    if continuer not in ("y", "o"):
      break

if __name__ == "__main__":
  main()



