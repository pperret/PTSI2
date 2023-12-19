def fact(n):
    '''Calcul de factorielle
    Paramètre:
    n: Entier naturel pour lequel la factorielle est à calculer
    Résultat: Valeur de la factorielle'''
    r = 1
    for i in range(1, n+1):
        r = r*i
    return r


def S(n):
    '''Fonction S
    Paramètre:
    n : Valeur devant être utilisée pour la fonction
    Résultat: Résultat de la fonction pour le paramètre d'entrée'''
    r = 0
    for k in range(0, n+1):
        r = r+k*fact(k)
    return r


def verification(n):
    '''Vérification de la relation pour une valeur particulière
    Paramètre:
    n : Valeur pour laquelle la vérification est à effectuer
    Résultat : True si la relation est vérifié et False sinon'''
    v = fact(n+1)-S(n)
    if v == 1:
        return True
    else:
        return False


# Boucle de vérification pour tous les entiers naturels inférieurs ou égaux à 100
ok = True
for i in range(0, 101):
    if verification(i) == False:
        ok = False

# Affichage du résultat
if ok:
    print("la relation est vérifiée")
else:
    print("la relation n'est pas vérifiée")
