import random


def alea(a, b, n):
    """ Génération d'une liste d'aléas (entiers ou flottants selon le type des bornes)
    Paramètres: Borne inférieure pour les aléas : a
    Borne supérieure pour les aléas : b
    Nombre d'aléas à générer : n
    Résultat: Liste des aléas générés"""
    # Initialisation de la liste résultat
    l = []

    # Il faut que b soit strictment supérieur à a
    if b > a:
        # Il faut que a et b soit du même type
        if type(a) == type(b):
            # Si a (et donc b) sont des entiers (comparaison en prenant le type d'une constante entière)
            if type(a) == type(1):
                # Génération de n entiers aléatoires dans la plage demandée
                for i in range(0, n):
                    l.append(random.randint(a, b))
            # Si a (et donc b) sont des flotants (comparaison en prenant le type d'une constante flottante)
            elif type(a) == type(1.):
                # Génération de n flottants aléatoires dans la plage demandée
                for i in range(0, n):
                    l.append(random.uniform(a, b))
                return l
            # Pour les autres types, rien à faire -> la liste résultante est vide
    return l


print(alea(1.5, 2., 5))
