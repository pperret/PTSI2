"""
Exercice 3 du TD4
"""
import matplotlib.pyplot as plt
import numpy as np

plt.close()

# Création du tableau contenant les valeurs de x (100 valeurs entre -5 et 5)
x = np.linspace(-5, 5, 100)

# Boucle pour m entre 0 et 5 inclus
for m in range(0, 6):
    # Calcul des valeurs y pour la valeur courante de m
    y = (1+m*x)/(1+x**2)

    # Affichage de la courbe
    plt.plot(x, y, label='m='+str(m))

# Affichage de la grille
plt.grid()

# Titre du graphique
plt.title('Courbes serpentines')

# Libellés pour les axes X et Y
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
