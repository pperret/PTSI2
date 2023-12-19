
import matplotlib.pyplot as plt
import math

# Purge d'un graphique existant
plt.close()

# Constantes
debut = 0  # Date de départ (s)
fin = 2  # Date de fin(s)
points = 200  # Nombre de points sur la courbe

# Valeurs calculées
pas = (fin-debut)/points  # Incrément temporel


def signal(t, A, f):
    '''Retourne la valeur du signal 
    Paramètres:
    t : Date à laquelle le signal est à calculer
    A : Amplitude du signal
    f : Fréquence du signal
    Résultat : Valeur calculée pour le signal en fonction des paramètres'''
    return A * math.sin(2*math.pi*f*t)


def lire_valeur(txt, min, max):
    '''Lecture d'une valeur flottante entre deux bornes
    Paramètres:
    txt : Invite d'entrée de la valeur
    min : Valeur minimale autorisée
    max : Valeur maximale autorisée
    Résultat: Valeur saisie'''
    while True:
        a = float(input(txt))
        if a >= min and a <= max:
            return a


# Lecture des valeurs (amplitude, fréquence)
amplitude = lire_valeur("Amplitude (de 1 à +10V) : ", 1, 10)
frequence = lire_valeur("Fréquence (de 1 à 20 Hz) : ", 1, 20)

# Initialisation des listes de valeurs (date et valeur du signal)
t = list()
s = list()

# Calcul des points sur la courbe
for i in range(0, points+1):
    tt = debut+pas*i
    ss = signal(tt, amplitude, frequence)
    t.append(tt)
    s.append(ss)

# Affichage de la courbe
plt.title("A="+str(amplitude)+" s, f=" + str(frequence)+" Hz")
plt.axis([debut, fin, -10, 10])
plt.xlabel("t(s)")
plt.ylabel("s(t)")
plt.plot(t, s)

# Nécessaire sur Mac
plt.show()
