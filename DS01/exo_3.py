import math


def S(n):
    '''Calcul de la somme géométrique
    Paramètre:
    n : Nombre d'itérations
    Résultat : Valeur de la suite pour le nombre d'itérations demandé'''
    r = 0
    for k in range(0, n+1):
        r = r+math.pow(0.5, k)
    return r


# Boucle tant que la différence est supérieure ou égale à 10E-10
n = 0
while abs(S(n)-2.0) >= 10E-10:
    n = n+1

print(n)
