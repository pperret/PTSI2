# NB: La fonction de l'exercice 1 est reprise (avec un return dans le cas False pour ne pas tester la suite lorsque c'est faux)
# car elle ne faisait pas d'hypothèse sur le fait que c'était des chiffres
def palin(n):
    '''Détermine si la chaîne d'entrée est un palindrome
    Paramètre: Chaine à tester n
    Résultat: True si la chaine est un palidrome, False si ce n'en est pas un
    '''
    for i in range(0, int(len(n)/2)):
        if n[i] != n[-i-1]:
            return False
    return True


# Saisie d'une chaîne
s = input('Donner une chaine : ')

# Détermine si c'est un palindrome et affiche le résultat
print(palin(s))
