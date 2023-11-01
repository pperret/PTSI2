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
dt = tau/10  # s
N = int(tf/dt)  # N doit être un nombre entier
# =============================================================================
# Fonctions
# =============================================================================


def F(u, E, tau):
    return (E-u)/tau


# =============================================================================
# Mise en oeuvre
# =============================================================================
# Boucle sur les différentes valeurs de dt
for dt1 in [tau/10, tau/5, tau/2]:
    # Nombre d'itérations pour une durée de 5 secondes en fonction de dt (N doit être un nombre entier)
    N1 = int(tf/dt1)
    u = [u0]  # liste des tensions calculées
    t = [0]  # liste des des dates considérées
    # Itérations pour chacune des dates (pas de dt)
    for i in range(0, N):
        t1 = t[-1]+dt1  # Calcul de la date
        u1 = u[-1] + F(u[-1], E, tau) * dt1  # Calcul de la tension pour la date
        # Ajout de la date et de la tension calculées aux tableaux résultants
        u.append(u1)
        t.append(t1)
    # Affiche de la courbe pour la valeur de dt considérée
    plt.plot(t, u, label='Euler pour '+str(round(dt*1e6, 2))+' μs')

# =============================================================================
# Calcul de la courbe analytique
# =============================================================================

# Initialisation du tableau des temps
t = np.linspace(0, tf, N)

# Calcul du tableau des tensions en utilisant les calculs sur les tableaux numpy
u = (u0 - E) * np.exp(-1 * t/tau) + E

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
