# -*- coding: utf-8 -*-
"""
Exercice 2 du TD4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

# Création du tableau contenant les valeurs de omegat (100 valeurs entre 0 et 2pi)
omegat = np.linspace(0, 2*np.pi, 100)

# Calcul des valeurs X et Y correspondant à omegat
x = 3*np.cos(omegat) - np.cos(3*omegat)
y = 3*np.sin(omegat) - np.sin(3*omegat)

# Affichage de la courbe
plt.plot(x, y)

# Affichage de la grille
plt.grid()

# Titre du graphique
plt.title('Courbe paramétrique')

# Libellés pour les axes X et Y
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
