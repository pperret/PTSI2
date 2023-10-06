def fac(n):
    '''Calcul de la factorielle d'un nombre
    Paramètre: Nombre dont la factorielle est à calculer n
    Résultat: Factorielle du nombre'''
    f = 1
    # Boucle de calcul de la factorielle
    # Commence à 2 car inutile pour la valeur 1
    for i in range(2, n+1):
        f = f*i
    return f


# Saisie du nombre dont la factorielle est à calculer
n = int(input('Donner un entier naturel : '))

# Calcul de la factorielle et affichage du résultat
print('Factorielle : ', fac(n))
