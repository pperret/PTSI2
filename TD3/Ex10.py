import math


def fac(n):
    '''Calcul de la factorielle d'un nombre
    Paramètre: Nombre dont la factorielle est à calculer n
    Résultat: Factorielle du nombre'''
    f = 1
    # Boucle de calcul de la factorielle
    # Commence à 2 car inutile pour la valeur 1
    for i in range(2, n+1):
        f *= i
    return f


def expo(x, n):
    '''Calcule une valeur approchée de l'exponentielle d'un nombre
    Paramètres: Nombre pour lequel l'exponentielle est à calculer x
    Nombre d'itérations pour la série n
    Résultat: Valeur approchée de l'exponentielle du nombre'''
    r = 0  # Initialisation du résultat
    # Boucle sur chaque terme de la série
    for i in range(0, n+1):
        # Utilisation de la fonction du package mathématique car l'écriture d'une fonction puissance
        # ne donne pas exactement le même résultat pour de grandes puissance ce qui provoque un résultat
        # général lègèrement différent (183505.5149043848 au lieu de 183505.51490438473)
        r += math.pow(x, i)/fac(i)
    return r


# Essai de la fonction
print(expo(12.12, 51))
