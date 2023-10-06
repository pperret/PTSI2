def pains(l, n):
    '''Duplique N fois chaque élément de la liste en entrée
    Paramètres: Liste dont chaque élément est à dupliquer l``
    Nombre de duplication à effectuer n
    Résultat: Liste dont chaque éléméent de la liste d'entrée a été dupliqué le nombre de fois demandé
    '''
    r = []  # Initialisation de la liste résultante
    # Boucle sur chaque élément de la liste d'entrée
    for e in l:
        # Boucle sur le nombre de duplication
        for i in range(0, n):
            r.append(e)
    return r


# Essai de la fonction
l = [2, 'toto', 12.12]
n = 3
print(pains(l, n))
