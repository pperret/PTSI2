# -*- coding: utf-8 -*-
"""
Mouvement d'un pendule avec la méthode d'Euler
"""
import matplotlib.pyplot as plt
import numpy as np
import math
plt.close('all')

# =============================================================================
# Données
# =============================================================================
theta0 = math.pi/2  # Angle initial (rad)
v0 = 0  # Vitesse angulaire initiale (rad/s)
g = 9.8  # Constante d'accélération (m/s2)
l = 0.5  # Longueur du fil (m)
tf = 10  # Durée du graphe (s)
dt = 0.01  # Pas (s)

# =============================================================================
# Grandeurs calculées
# =============================================================================
N = int(tf/dt)  # Nombre de points

# =============================================================================
# Fonctions
# =============================================================================


def F(theta, g, l):
    '''Calcul de l'accélération angulaire pour un angle
    Paramètres: Valeur de l'angle theta (rad)
    Constante d'accélération g (m/s2)
    Longueur du fil l (m)
    Résultat: Accélération pour l'angle spécifié (rad/s2)'''
    return -g/l*math.sin(theta)


def vitesse(vc, gc, dt):
    '''Calcul de la vitesse angulaire pour la date suivante en fonction de la vitesse à la date courante
    Paramètres: Vitesse angulaire pour la date courante vc (rad/s)
    Accélération pour la date courante gc (rad/s2)
    Pas de temps dt (s)
    Résultat: Vitesse pour la date suivante (rad/s)'''
    return vc + gc * dt


def angle(thetac, vc, dt):
    '''Calcul de l'angle pour la date suivante en fonction de l'angle à la date courante
    Paramètres: Angle pour la date courante thetac (rad)
    Vitesse angulaire pour la date courante vc (rad/s)
    Pas de temps dt (s)
    Résultat: Angle pour la date suivante (rad)'''
    return thetac + vc * dt


# =============================================================================
# Mise en oeuvre
# =============================================================================
theta = [theta0]  # liste des angles calculés
v = v0  # Vitesse courante
t = [0]  # liste des dates considérées

# Itération pour chacune des N dates
for i in range(1, N+1):
    # Calcul de la date courante et ajout à la liste
    t.append(dt*i)
    # Calcul de la vitesse angulaire courante par rapport à la précédente
    v2 = vitesse(v, F(theta[-1], g, l), dt)
    # Calcul de l'angle courant par rapport au précédent
    theta.append(angle(theta[-1], v, dt))
    # L'utilisation de la formule ci-dessus produit un graphe qui diverge.
    # (cf. https://www.physagreg.fr/methodes-numeriques-euler-runge-kutta.php)
    # Pour que cela ne diverge pas (toujours d'après l'article), il faut utiliser la formule suivante
    # theta.append(angle(theta[-1], v2, dt))
    # Mise à jour de la vitesse courante
    v = v2

# =============================================================================
# Graphe de la solution numérique
# =============================================================================
plt.plot(t, theta, label='Euler pour '+str(round(dt*1e3, 2))+' ms')
plt.grid()
plt.xlabel("t (en s)")
plt.ylabel("theta(t) (en radians)")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
