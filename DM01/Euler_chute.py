# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:23:27 2023

@author: LnX
"""
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

# =============================================================================
# Données
# =============================================================================
v0 = 0  # Vitesse initiale (m/s)
g = 9.8  # Constante d'accélération (m/s2)
k = 4E-2  # Coefficient de frottement (kg/m)
m = 0.2  # Masse de l'objet (kg)
tf = 4  # Durée du graphe (s)
N = 100  # Nombre de points sur le graphe

# =============================================================================
# Grandeurs calculées
# =============================================================================
dt = tf/N  # Calcul du pas en fonction de la durée et du nombre de points (s)

# =============================================================================
# Fonctions
# =============================================================================


def F(v, k, m, g):
    '''Calcul de la dérivée de la vitesse pour la date courante
    Paramètres: Vitesse pour la date courante v
    Coefficient de frottement k
    Masse de l'objet m
    Constante d'accélération g
    Résultat: Dérivée de la vitesse à la date courante'''
    return g - k/m*v*v


def vitesse(v, k, m, g, dt):
    '''Calcul de la vitesse pour la date suivante en fonction de la date courante
    Paramètres: Vitesse pour la date courante v
    Coefficient de frottement k
    Masse de l'objet m
    Constante d'accélération g
    Pas de temps dt
    Résultat: Vitesse pour la date suivante'''
    return v + F(v, k, m, g) * dt


# =============================================================================
# Mise en oeuvre
# =============================================================================
v = [v0]  # liste des vitesses calculées
t = [0]  # liste des des dates considérées

# Itération ppour chacune des N dates
for i in range(1, N+1):
    # Calcul de la date courante et ajout à la liste
    t.append(dt*i)
    # Calcul de la vitesse pour la date courante (à partir de la valeur précédente) et ajout à la liste
    v.append(vitesse(v[-1], k, m, g, dt))

# =============================================================================
# Graphe de la solution numérique
# =============================================================================
plt.plot(t, v, label='Euler pour '+str(round(dt*1e3, 2))+' ms')
plt.grid()
plt.xlabel("t")
plt.ylabel("v(t)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()

# Au bout de deux secondes, la vitesse maximale est quasiment atteinte
# Les frottements compensent alors la gravité ce qui empêche l'accroisement de la vitesse
