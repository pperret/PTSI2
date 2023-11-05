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
dt = tau/10  # Pas de temps (s)
N = int(tf/dt)  # Nombre de points sur le graphe (N doit être un nombre entier)

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


def tension_analytique(t, E, u0, tau):
    ''' Calcul en mode analytique des tensions pour un tableau numpy de dates
     Paramètres: Tableau numpy des dates t
     Tension du générateur E
     Tension initiale du condensateur u0
     Constante de temps tau
     Résultat: Tableau numpy des tensions calculées'''
    return (u0 - E) * np.exp(-1 * t/tau) + E


# =============================================================================
# Mise en oeuvre
# =============================================================================
# Boucle sur les différentes valeurs de dt
for dt1 in [tau/10, tau/5, tau/2]:
    # Nombre d'itérations en fonction de dt (N doit être un nombre entier)
    N1 = int(tf/dt1)
    u = [u0]  # liste des tensions calculées
    t = [0]  # liste des des dates considérées

    # Itérations pour chacune des N dates (avec un pas de dt)
    for i in range(1, N1+1):
        # Calcul de la date courante et ajout à la liste
        t.append(i*dt1)
        # Calcul de la tension pour la date courante en fonction de la précédente et ajout à la liste
        u.append(tension(u[-1], E, tau, dt1))

    # Affiche de la courbe pour la valeur de dt considérée
    plt.plot(t, u, label='Euler pour '+str(round(dt*1e6, 2))+' μs')

# =============================================================================
# Calcul de la courbe analytique
# =============================================================================

# Initialisation du tableau des temps
t = np.linspace(0, tf, N)

# Calcul du tableau des tensions en utilisant les calculs sur les tableaux numpy
u = tension_analytique(t, E, u0, tau)

# Affichage du résultat
plt.plot(t, u, label='Courbe analytique')

# =============================================================================
# Affichage du fond du graphe
# =============================================================================
plt.grid()
plt.xlabel("t")
plt.ylabel("u(t)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()

# On voit que plus le pas est faible, plus la courbe résultante se rapproche de la courbe théorique
