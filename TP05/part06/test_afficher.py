# -*- coding: utf-8 -*-
"""
@author: Ppt
"""

def afficher(l):
    '''
    Paramètre : liste de caractères l
    Résultat : None. 
    Affiche une chaine de caractères contenant les caractères de la liste avec des espaces
    Par exemple la liste ['d','_','n','_','l','d'] conduit à afficher la chaîne 'd _ n _ l d'        
    '''
    assert type(l) is list, "Le paramèrte de afficher() n'est pas une liste"
    for c in l:
        assert type(c) is str and len(c)==1, "Un des éléments de la liste n'est pas un caractère"
    ch=''
    for e in l:
        ch+=e
    print(ch)

# Cas normal
l=['a', '_', '_', 'd', 'e']
afficher(l)

# Cas limite avec une liste vide
l=[]
afficher(l)

# Cas anormal avec un élément qui n'est pas un caractère mais une chaine => erreur
l=['a', '_', '_', 'dd', 'e']
#afficher(l)

# Cas anormal avec un élément qui n'est pas un caractère mais un entier => erreur
l=['a', '_', '_', 10, 'e']
#afficher(l)

# Cas anormal avec un entier en paramètre => erreur
#afficher(10)

