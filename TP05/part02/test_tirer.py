# -*- coding: utf-8 -*-
"""
@author: Ppt
"""

import random
import sys


def tirer(l):
    '''
    Paramètre : liste l
    Résultat : retourne un élément de la liste l choisi aléatoirement
    '''
    # Je ne sais si vous avez déjà vu cela
    assert type(l) is list, "Le paramètre de 'tirer()' n'est pas une liste."
    assert len(l) > 1, "Le nombre d'éléments de la liste est inférieur à 2."
    n = random.randint(0, len(l)-1)
    return l[n]


# Pas une liste => erreur
x = 1
#print(tirer(x))

# Liste vide => erreur
l0 = []
#print(tirer(l0))

# Liste d'un élément => erreur
l1 = [1]
#print(tirer(l1))

# Liste avec plus de 1 élément => Fournit des résultats aléatoires
l = [10, 20, 30, 5, 15, 25]
print(tirer(l))
print(tirer(l))
print(tirer(l))
print(tirer(l))
print(tirer(l))
print(tirer(l))
print(tirer(l))
