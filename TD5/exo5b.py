# -*- coding: utf-8 -*-
"""
Exercice 5b du TD5
"""

mots = ['Raphael', 'Lea', 'Celia', 'Armando', 'Alexandre', 'Pierre-Antoine', 'Arno', 'Matis', 'Yohan', 'Thomas', 'Benjamin', 'Ninon', 'Achille', 'Alban', 'Tristan', 'Jeanne', 'Amaury', 'Maximilien', 'Antoine',
        'Clemence', 'Nathan', 'Gauthier', 'Guillaume', 'Elias', 'Matt', 'Victor', 'Quentin', 'Kelian', 'Eliot', 'Barthelemi', 'Luna', 'Gatien', 'Mathys', 'Mathis', 'Pierre', 'Nicolas', 'Xavier', 'Robin', 'Florelle', 'Julien']


def creerdico(liste):
    '''Génération d'un dictionnaire dont chaque entrée est la liste des mots ayant une lettre (sans tenir compte des majuscules/minuscules) à une position donnée
    Paramètres : Liste des mots à analyser liste
    Résultat: Dictionnaire contenant l'indexation des lettres à une position donnée'''
    # Initialisation du dictionnaire
    dico = dict()
    # Boucle sur la liste des mots en entrée
    for mot in liste:
        # Enumération de chaque lettre du mot (avec sa position)
        for index, value in enumerate(mot):
            # Passage de la lettre en minuscule car les recherches ne tiennent pas compte des majuscules/minuscules
            lettre = value.lower()
            # Ajout du mot au dictionnaire indexé par le tupple (position, lettre)
            # Il faut ajouter 1 à l'index pour que la première lettre du mot corresponde à la valeur 1 et non 0
            dico[(index+1, lettre)] = dico.get((index+1, lettre), []) + [mot]
    return dico


def mlp(dico, lettre, position):
    ''' Recehrche dans le dictionnaire les mots ayant la lettre demandée (sans tenir compte des majuscules/minuscules) à la position indiquée
    Paramètres : Dictionnaire des mots dico
    Lettre à rechercher lettre
    Position de la lettre à rechercher (1 = première lettre) position
    '''
    # Lors de la recherche dans le dictionnaire, la lettre est convertie en minuscule afin que la recherche ne tiennent pas compte
    # des majuscules/minuscules
    return dico.get((position, lettre.lower()))


# Création du dictionnaire à partir de la liste des mots
dico = creerdico(mots)

# Affichage du dictionnaire
print(dico)

print(mlp(dico, 'e', 3))
print(mlp(dico, 'a', 2))
print(mlp(dico, 'y', 5))
