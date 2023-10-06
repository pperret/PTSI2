
def scrabble_lettre(l):
    """Détermine la valeur d'une lettre au scrabble
    Paramètre : Lettre dont la valeur est à déterminer : l
    Résultat: Valeur de la lettre"""

    if l in 'AEILNORSTU':
        return 1
    elif l in 'DGM':
        return 2
    elif l in 'BCP':
        return 3
    elif l in 'FHV':
        return 4
    elif l in 'JQ':
        return 8
    elif l in 'KWXYZ':
        return 10
    else:
        return 0  # Pas une lettre


def scrabble(ch):
    """Détermine la valeur d'une chaîne de caratères au scrabble
    Paramètre : Chaine dont la valeur est à calculer : ch
    Résultat : Valeur de la chaine au scrabble"""

    # Initialisation de la somme des valeurs de chaque caractèr
    s = 0

    # Boucle sur les lettres de la chaine convertie en majuscules
    # pour avoir leur valeur individuelle et l'ajouter au cumul
    for c in ch.upper():
        s += scrabble_lettre(c)
    return s


# Essais de la fonction
print(scrabble('prachay'))
print(scrabble('bovetto'))
print(scrabble('lanoix'))
