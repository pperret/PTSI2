# Initialisation des listes
pairs = []
impairs = []

# Boucle de saisie des nombres entiers
fini = False
while not fini:
    chaine = input('Entrez un nombre entier (STOP pour arrêter) : ')

    # Test de fin de saisie
    if chaine == 'STOP':
        fini = True

    # Vérification que la valeur saisie est un entier
    elif chaine.isdigit() == False:
        print('Veuillez saisir un nombre entier ou STOP')

    # Ajout de la valeur saisie à la liste correspondante
    else:
        # Conversion de la chaine en entier (ne peut pas échouer suite à la vérification précédente)
        nombre = int(chaine)

        # Détermine si le nombre est pair ou impair en fonction de son modulo 2
        if nombre % 2 == 0:
            pairs.append(nombre)
        else:
            impairs.append(nombre)

# Affichage des deux listes résultantes
print(pairs)
print(impairs)
