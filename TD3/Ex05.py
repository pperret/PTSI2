import math


def premier1(n):
    '''Détermine si un entier naturel est premier (version naïve)
    Paramètre: Nombre dont la primalité est à tester n
    Résultat: True si le nombre est premier, False si ce n'est pas le cas'''
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def premier2(n):
    '''Détermine si un entier naturel est premier (version optimisée)
    Paramètre: Nombre dont la primalité est à tester n
    Résultat: True si le nombre est premier, False si ce n'est pas le cas'''
    # Test si le nombre est pair
    if n % 2 == 0:
        return False
    # Test à partir de 3 en sautant les nombres pairs et à s'arrêtant à la racine carrée du nombre
    for i in range(3, int(math.sqrt(n))+2, 2):
        if n % i == 0:
            return False
    return True


# Saisie d'un nombre dont la primalité est à tester
n = int(input('Donner un nombre : '))

# Détermination de la primalité et affichage du résultat selon les deux méthodes
print('Version naïve :', premier1(n))
print('Version optimisée :', premier2(n))
