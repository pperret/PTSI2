"""
Exercice 5 du TD4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

# Augmente la largeur affichée pour correspondre au format demandé
# cf. documentation sur Internet
plt.figure().set_figwidth(10)

# Création du tableau contenant les valeurs de t (100 valeurs entre 0 et 5)
x = np.linspace(-np.pi, np.pi, 100)

# Boucle sur les valeurs de m
for m in [1, 2, 3, 4, 5, 6, 7]:
    # Calcul des valeurs de Y
    y = np.sin(m*x)/m
    # Tracé de la courbe
    plt.plot(x, y, label='m='+str(m))

# Affichage de la grille
plt.grid()

# Libellés pour les axes X et Y
plt.xlabel("x")
plt.ylabel("f(x)")

# Les arguments permettent d'avoir la taille des caractères et la position des libellés demandés
# cf. documentation sur Internet
plt.legend(loc='upper right', fontsize=5)

# ATTENTION : Nécessaire sur MAC
plt.show()
