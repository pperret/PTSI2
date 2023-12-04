# -*- coding: utf-8 -*-
"""
Exercice 5a avec perfs du TD5
"""
import time

mots = ['Raphael', 'Lea', 'Celia', 'Armando', 'Alexandre', 'Pierre-Antoine', 'Arno', 'Matis', 'Yohan', 'Thomas', 'Benjamin', 'Ninon', 'Achille', 'Alban', 'Tristan', 'Jeanne', 'Amaury', 'Maximilien', 'Antoine',
        'Clemence', 'Nathan', 'Gauthier', 'Guillaume', 'Elias', 'Matt', 'Victor', 'Quentin', 'Kelian', 'Eliot', 'Barthelemi', 'Luna', 'Gatien', 'Mathys', 'Mathis', 'Pierre', 'Nicolas', 'Xavier', 'Robin', 'Florelle', 'Julien']


def mlp(liste, lettre, position):
    '''  
   Parameters
    ----------
    liste : TYPE liste de mots (chaînes de caractères alphanumériques)
        DESCRIPTION : Liste des mots à analyser.
    lettre : TYPE caractère alphanumérique
        DESCRIPTION : Lettre à rechercher.
    position : TYPE entier
        DESCRIPTION: Position de la lettre à rechercher (1 = première lettre).

    Returns
    -------
    res : TYPE liste de mots
        DESCRIPTION : liste des mots de la liste d'entrée admettant le caractère donné à la position donnée
    '''
    # Passage de la lettre en minuscule (la recherche ne tient pas compte des majuscules/minuscules)
    lettre = lettre.lower()
    # Initialisation de la liste résultante
    res = []
    # Boucle sur les mots de la liste d'entrée
    for mot in liste:
        # Détermine si la lettre recherche est bien à la bonne place dans le mot
        # Auparavent, il faut s'assurer que la longueur du mot n'est pas plus petite que la position demandée
        if len(mot) >= position and mot[position-1].lower() == lettre:
            # Si cela correspond, le mot est ajouté à la liste résultat
            res.append(mot)
    return res


# ATTENTION : J'ai fait un programme dédié car je n'ai pas le F9
tic = time.perf_counter()
for i in range(0, 100000):
    l = mlp(mots, 'e', 5) + mlp(mots, 'a', 2) + \
        mlp(mots, 'y', 5) + mlp(mots, 't', 3) + mlp(mots, 'h', 4)
tac = time.perf_counter()
print(tac-tic)
