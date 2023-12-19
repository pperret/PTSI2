import matplotlib.pyplot as plt

# Purge d'un graphique existant
plt.close()

# Valeurs initiales et constantes
v0 = -10  # en m/s
m = 0.3  # en kg
k = 0.015  # en USI
tmin = 0  # en s
tmax = 10  # en s
points = 200  # Nombre de points dans la courbe
g = 9.8  # en m/s2

# Valeurs calculées
dt = (tmax-tmin)/points


def F(v):
    return -k/m*v*v+g


# Initialisation des listes avec les valeurs initiales
t = [0]
v = [v0]

# Calcul des points sur la courbe
for i in range(1, points):
    t.append(t[-1]+dt)
    v.append(F(v[-1])*dt+v[-1])

# Affichage de la courbe
plt.title("Ca frotte")
plt.xlabel("t(s)")
plt.ylabel("v(t)")
plt.plot(t, v)

# Nécessaire sur Mac
plt.show()
