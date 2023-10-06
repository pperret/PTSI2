def is_in(c, L):
    '''Détermine si un caractère est présent dans une liste
    Paramètres: Caractère à rechercher c
    Liste de caractères dans laquelle la recherche est effectuée L
    Résultat: True si le caractère a été trouvé, False si ce n'est pas le cas
    '''
    for cl in L:
        if cl == c:
            return True
    return False


# Essais de la fonction
print(is_in('c', ['a', 'b', 'd', 'C']))
print(is_in('c', ['a', 'b', 'c', 'd', 'C']))
