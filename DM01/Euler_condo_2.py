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
u0 = 0  # Tension initiale pour le condensateur (V)
E = 10  # Tension du générateur (V)
R = 1000  # Valeur de la résistance (ohm)
C = 1E-9  # Valeur de la capacité (F)

# =============================================================================
# Grandeurs calculées
# =============================================================================
tau = R*C  # Constante de temps (s)
tf = 5*tau  # Durée du graphe (s)

# =============================================================================
# Fonctions
# =============================================================================


def F(u, E, tau):
    '''Calcul de la dérivée de la tension pour la date courante
    Paramètres: Tension pour la date courante u
    Tension du générateur
    Constante de temps tau
    Résultat: Dérivée de la tension à la date courante'''
    return (E-u)/tau


def tension(u, E, tau, dt):
    '''Calcul de la tension pour la date suivante en fonction de celle pour la date courante
     Paramètres: Tension pour la date courante u
     Tension du générateur E
     Constante de temps tau
     Pas de temps dt
     Résultat: Tension à la date suivante'''
    return u + F(u, E, tau)*dt


# =============================================================================
# Mise en oeuvre
# =============================================================================
# Boucle sur les différentes valeurs de dt
for dt in [tau/10, tau/5, tau/2]:
    # Nombre d'itérations en fonction de dt (N doit être un nombre entier)
    N = int(tf/dt)
    u = [u0]  # liste des tensions calculées
    t = [0]  # liste des des dates considérées

    # Itérations pour chacune des N dates (avec un pas de dt)
    for i in range(1, N+1):
        # Calcul de la date courante et ajout à la liste
        t.append(i*dt)
        # Calcul de la tension pour la date courante en fonction de la précédente et ajout à la liste
        u.append(tension(u[-1], E, tau, dt))

    # Affiche de la courbe pour la valeur de dt considérée
    plt.plot(t, u, label='Euler pour '+str(round(dt*1e6, 2))+' μs')

# =============================================================================
# Affichage du fond du graphe
# =============================================================================
plt.grid()
plt.xlabel("t")
plt.ylabel("u(t)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
