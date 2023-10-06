def syracuse(u0):
    '''Détermine l'indice du premier terme valant 1 dans la suite de Syracuse à partir d'un nombre donné
    Paramètre: Nombre de départ pour la suite u0
    Résultat: Indice du premier terme valant 1
    '''
    un = u0  # Affecte la valeur courante de Un
    n = 0  # Initialisation du compteur
    # Boucle tant que la valeur 1 n'a pas été rencontrée
    while un != 1:
        # Calcul de la valeur suivante dans la série
        if un % 2 == 0:
            un = un/2
        else:
            un = 3*un+1
        n += 1  # Incrément du compte
    return n


# Saisie d'un entier
n = int(input('Donner un entier : '))

# Calcul de l'indice du premier terme valant 1 et affichage du résultat
print(syracuse(n))
