# -*- coding: utf-8 -*-
"""
Exercice 4 du TD4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

# Données
sm1 = 2  # (en m)
f1 = 3  # (en Hz)
phi1d = 10  # (en degrés)
sm2 = 2  # (en m)
f2 = 3.5  # (en Hz)
phi2d = 0  # (en degrés)

# Conversion degrés=>radians
phi1 = phi1d*np.pi/180
phi2 = phi2d*np.pi/180

# Création du tableau contenant les valeurs de t (100 valeurs entre 0 et 5)
t = np.linspace(0, 5, 500)

# Calcul de s1 et s2
s1 = sm1 * np.cos(2*np.pi*f1*t+phi1)
s2 = sm2 * np.cos(2*np.pi*f2*t+phi2)

# Calcul du produit s1*s2
s1s2 = s1*s2

# Tracé de la courbe
plt.plot(t, s1s2)

# Affichage de la grille
plt.grid()

# Titre du graphique
plt.title("Produit d'amplitudes")

# Libellés pour les axes X et Y
plt.xlabel("t")
plt.ylabel("s1(t)*s2(t)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
