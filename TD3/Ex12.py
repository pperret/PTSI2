import math


def somme(p, n):
    """ Calcule le résulat de la somme d'une série spécifique
    Paramètres: Exposant à utiliser : p
    Nombre d'itérations : n
    Résultat : Somme de la série"""
    s = 0
    for k in range(1, n+1):
        s += 1/math.pow(k, p)
    return s


l = [10, 50, 100, 500, 5000, 50000, 500000]

p = int(input("Donner l'entier naturel p : "))

for n in l:
    print('Pour p =', p, 'et n=', n, ': S_p(n) = ', somme(p, n))

# Lorsque n tend vers l'infini, le résultat tend vers une valeur finie
