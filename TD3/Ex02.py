def pgcd(v1, v2):
    '''Détermine le PGCD de deux nombres naturels
    Paramètres: Nombres pour lesquels le PGCD doit être calculé v1, v2
    Résultat: PGCD des deux nombres'''
    if v2 > v1:
        v1, v2 = v2, v1

    while v1 != 0:
        while v1 >= v2:
            v1 = v1-v2
        if v1 != 0:
            v1, v2 = v2, v1
    return v2


# Saisie des deux nombres dont le PGCD doit être calculé
n1 = int(input('Saisir le premier entier : '))
n2 = int(input('Saisir le second entier : '))

# Calcul du PGCD et affichage du résultat
print('pgcd :', pgcd(n1, n2))
