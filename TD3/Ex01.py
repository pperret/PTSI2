def palin(n):
    '''Détermine si la chaîne d'entrée est un palindrome
    Paramètre: Chaine à tester n
    Résultat: True si la chaine est un palidrome, False si ce n'en est pas un
    '''
    d = True
    for i in range(0, int(len(n)/2)):
        if n[i] != n[-i-1]:
            d = False
    return d


def somme(n):
    '''Calcule la somme des chiffres d'un nombre passé sous la forme d'une chaine
    Paramètre: Nombre sous la forme d'une chaine n
    Résultat: Somme des chiffres du nombre
    '''
    s = 0
    for c in n:
        s = s+int(c)
    return s


# Initialisation du cumul des sommes des chiffres des palidromes
s = 0

# Boucle sur les nombres à 4 chiffres (de 1000 à 9999)
for i in range(1000, 10000):
    n = str(i)  # Conversion du nombre sous la forme d'une chaine
    # Si c'est un palidrome, la somme de ses chiffres est ajouté au cumul
    if palin(n):
        s = s+somme(n)
# Affichage du cumul
print(s)
