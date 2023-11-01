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
u0 = 0  # V
E = 10  # V
R = 1000  # ohm
C = 1E-9  # F

# =============================================================================
# Grandeurs calculées
# =============================================================================
tau = R*C  # s
tf = 5*tau  # s

# =============================================================================
# Fonctions
# =============================================================================


def F(u, E, tau):
    return (E-u)/tau


# =============================================================================
# Mise en oeuvre
# =============================================================================
# Boucle sur les différentes valeurs de dt
for dt in [tau/10, tau/5, tau/2]:
    # Nombre d'itérations pour une durée de 5 secondes en fonction de dt (N doit être un nombre entier)
    N = int(tf/dt)
    u = [u0]  # liste des tensions calculées
    t = [0]  # liste des des dates considérées
    # Itérations pour chacune des dates (pas de dt)
    for i in range(0, N):
        t1 = t[-1]+dt  # Calcul de la date courante
        # Calcul de la tension pour la date courante
        u1 = u[-1] + F(u[-1], E, tau) * dt
        # Ajout de la date et de la tension calculées aux tableaux résultants
        u.append(u1)
        t.append(t1)
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
