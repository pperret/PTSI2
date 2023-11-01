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
v0 = 0  # m/s
g = 9.8  # m/s2
k = 4E-2  # kg/m
m = 0.2  # kg
tf = 4  # s

# =============================================================================
# Grandeurs calculées
# =============================================================================
N = 100  # Nombre de points sur le graphe
dt = tf/N  # Calcul du pas en fonction de la durée et du nombre de points (s)

# =============================================================================
# Fonctions
# =============================================================================


def F(v, k, m, g):
    return g - k/m*v*v


# =============================================================================
# Mise en oeuvre
# =============================================================================
v = [v0]  # liste des vitesses calculées
t = [0]  # liste des des dates considérées
# Itération sur les N-1 dates restantes (t[0] correspond aux conditions initiales)
for i in range(0, N):
    t1 = t[-1]+dt  # Caclcul de la date
    v1 = v[-1] + F(v[-1], k, m, g) * dt  # Calcul de la vitesse pour la date
    # Ajout de la date et de la vitesse calculées aux tableaux résultants
    v.append(v1)
    t.append(t1)

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
