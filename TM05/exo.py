# -*- coding: utf-8 -*-
"""
Répertoire téléphonique basé sur un dictionnaire
"""

# Dictionnaire du répertoire avec son contenu initial
d = {'Lanoix': '0123456789', 'Prachay': '1234567890', 'Bovetto': '2345678901'}


def ajoute(d, nom, numero):
    '''Ajout une entrée dans le répertoire
    Paramètres :
    d : Dictionnaire contenant le répertoire
    nom : Nom de l'entrée à ajouter
    numero : Numéro de téléphone de l'entrée à ajouter
    Résultats :
    Dictionnaire modifié avec la nouvelle entrée (ou dont une entrée existante a eu son numéro mis à jour)'''
    d[nom] = numero
    return d


def affiche(d):
    '''Affiche le contenu du répertoire
    Paramètres :
    d : Dictionnaire contenant le répertoire
    Résultats :
    Néant'''
    for (nom, numero) in d.items():
        print(nom, numero)


def recherche(d, chaine):
    '''Recherche une entrée dans le répertoire et affiche le nom correspondant
    Un message spécifique est affiché si le nom n'est pas présent dans le répertoire
    Paramètres :
    d : Dictionnaire contenant le répertoire
    chaine : Nom de l'entrée à rechercher dans le répertoire
    Résultats :
    Néant'''
    numero = d.get(chaine)
    if numero == None:
        print("Le contact", chaine, "n'est pas dans le répertoire")
    else:
        print("Le numéro de", chaine, "est", numero)


# Boucle tant que l'utilisateur n'a pas choisi de quitter
fini = False
while not fini:
    # Saisie du choix de l'utilisateur
    choix = input(
        "Choisir :\n 0 pour quitter\n 1 pour ajouter un contact\n 2 pour tout afficher\n 3 pour rechercher un contact\n")
    # Traitement selon le choix de l'utilisateur
    if choix == "0":
        fini = True
    elif choix == "1":
        nom = input("Nom du contact : ")
        numero = input("Numéro de téléphone : ")
        d = ajoute(d, nom, numero)
    elif choix == "2":
        affiche(d)
    elif choix == "3":
        nom = input("Nom du contact à rechercher : ")
        recherche(d, nom)
    else:
        print("Choix invalide")

# Affichage du message de fin
print("Bye")
