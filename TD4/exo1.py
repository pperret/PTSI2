# -*- coding: utf-8 -*-
"""
Exercice 1 du TD4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

# Création du tableau contenant les valeurs de X (100 valeurs entre -0,1 et 5)
x = np.linspace(-0.1, 5, 100)

# Calcul des valeurs Y correspondantes
y = x*np.exp(-2*x)

# Affichage de la courbe
plt.plot(x, y)

# Affichage de la grille
plt.grid()

# Titre du graphique
plt.tile('Courbe f(x) = x exp(-2x)')

# Libellés pour les axes X et Y
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
