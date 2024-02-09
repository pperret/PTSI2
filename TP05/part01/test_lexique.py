# -*- coding: utf-8 -*-
"""
@author: Ppt
"""


def lexique(f):
    '''
    Paramètre : fichier f (chaîne de caractères) présent dans le dossier courant contenant un mot par ligne
    Résultat : liste contenant les mots du fichier
    '''
    lex = []
    fichier = open(f, 'r')
    for ligne in fichier:
        lex.append(ligne.strip('\n'))
    fichier.close()
    return lex


lst = lexique("lexique.txt")
print("Nombre d'éléments de la liste :", len(lst))

# La réponse est 13736
