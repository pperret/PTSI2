"""
Exercice 3 du TD5
"""

# Valeur de chaque lettre au scrabble
scrabble = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2,
            'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}


def points(mot):
    '''' Calcul le score d'un mot au scrabble
    Parametres: 
        mot : Mot dont le score doit être calculé

    Résultat: 
        score : Score correspondant au mot fourni en entrée
    '''
    # Initialisation du score
    score = 0
    # Boucle sur chaque caractère du mot
    for c in mot:
        # Passage de la lettre en majuscule car la clé du dictionnaire contient des lettres majuscules
        # pour traiter indifférement majuscules/minuscules dans le mot en entrée
        c = c.upper()
        # Les caractères non valorisés au scrabble sont ignorés
        if c in scrabble:
            score += scrabble[c]
    return score


# Tests basiques de la fonction points
print("voiture:", points("voiture"))
print("wagon:", points("wagon"))
