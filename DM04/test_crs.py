#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Test of the Crazy Random Sort
"""
import random
import time
import matplotlib.pyplot as plt

# =============================================================================
# Crazy Random Sort
# =============================================================================


def melange_liste(l):
    ''' Mélange aléatoirement la liste avec la méthode de Fisher-Yates.
    Paramètres :
        l : Liste à mélanger
    Résultat: 
        Aucun
    '''
    for i in range(len(l)-1, 0, -1):
        j = random.randint(0, i)
        l[i], l[j] = l[j], l[i]


def est_triee(l):
    '''Détermine si la liste est triée.
    Paramètres :
        l : Liste à vérifier si triée ou non.
    Résultat : 
        True si la liste est triée, False sinon.
    '''
    return all(l[i] <= l[i + 1] for i in range(len(l)-1))


def CRS(l):
    '''Trie la liste en utilisant la méthode du Crazy Random Sort.
    Paramètres:
        l : Liste à trier
    Résultat: 
        Aucun
    '''
    while not est_triee(l):
        melange_liste(l)

# =============================================================================
# Tri_rapide
# =============================================================================


def tri_rapide(liste):
    '''Trie la liste par ordre croissant en utilisant l'algorithme du tri rapide.
    Paramètres:
        liste : Liste à trier.
    Résultat : 
        Liste triée par ordre croissant.
    '''
    if liste == []:
        return liste
    liste_g = []
    liste_d = []
    for i in range(1, len(liste)):
        if liste[i] <= liste[0]:
            liste_g.append(liste[i])
        else:
            liste_d.append(liste[i])
    return tri_rapide(liste_g)+[liste[0]]+tri_rapide(liste_d)

# =============================================================================
# Fonction chronomètre pour le QS et CRS
# =============================================================================


def chrono(l, f):
    '''Mesure le temps nécessaire pour trier la liste l avec la fonction de tri f.
    Paramètres:
        l : Liste à trier
        f : Fonction de tri (QS ou CRS)
    Résultat : 
        Temps nécessaire pour trier la liste en secondes.
    '''
    debut = time.perf_counter()
    f(l)
    fin = time.perf_counter()
    return fin-debut


def genere_liste_majuscules(lg):
    '''Génère une liste de majuscules aléatoires
    Paramètres:
        lg : Longueur de la liste à générer
    Résultat :
        Liste de majuscules aléatoires
    '''
    majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return [majuscules[random.randint(0, 25)] for i in range(lg)]


plt.close('all')
plt.title('CRS vs. QS pour le même travail sur des listes de 0 à 10 éléments')
plt.grid()
plt.xlabel("Quick Sort (en s)")
plt.ylabel("Crazy Random Sort (en s)")
for i in range(11):
    l_crs = genere_liste_majuscules(i)
    l_qs = l_crs.copy()
    t_crs = chrono(l_crs, CRS)
    t_qs = chrono(l_qs, tri_rapide)
    plt.plot(t_qs, t_crs, "bx")

# Nécessaire sur Mac
plt.show()
