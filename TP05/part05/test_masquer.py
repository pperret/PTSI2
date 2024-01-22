# -*- coding: utf-8 -*-
"""
@author: Ppt
"""

def masquer(ch):
    """
    Paramètre : Chaîne de caractères ch
    Résultat : liste de '_' en même quantité que le nombre de lettres de ch
        affiche le nombre de lettres que possède la chaîne ch
    """
    assert type(ch) is str, "Le paramètre de masquer n'est pas une chaîne de caractères"
    l=[]
    for c in ch:
        l+='_'
    print('Le mot à trouver avec moins de 10 erreurs possède',len(l),'lettres')
    return l


# Cas normal
s = masquer("anticonstitutionnellement")
print("Pour anticonstitutionnellement :", s)

# Cas limite avec une chaine vide
s = masquer("")
print("Pour une chaîne vide: ", s)

# Pas une chaine => erreur
s = masquer(10)