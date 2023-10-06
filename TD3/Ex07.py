def pair(l):
    '''Détermine le nombre d'entiers pairs dans une liste
    Paramètre: Liste d'entiers l
    Résultat: Nombre d'entiers pairs trouvés dans la liste
    '''
    n = 0  # Initilisation du nombre d'entiers pairs trouvés
    for i in l:
        if i % 2 == 0:
            n = n+1
    return n


# Essais de la fonction
print(pair([12, 13, 20, 24]))
print(pair([12, 14, 20, 24]))
print(pair([11, 13, 1, 23]))
print(pair([]))
