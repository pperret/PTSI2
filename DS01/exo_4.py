import matplotlib.pyplot as plt
# Purge d'un graphique existant
plt.close()

# Valeurs initiales
u0 = 2
v0 = -1

# Création des listes
n = list()
u = list()
v = list()

# Ajout des valeurs initiales aux listes
n.append(0)
u.append(u0)
v.append(v0)

# Calcul des 16 premiers termes (sans compter les valeurs initiales)
for n1 in range(1, 17):
    n.append(n1)
    u1 = 2*u[-1]-v[-1]
    v1 = u[-1]+4*v[-1]
    u.append(u1)
    v.append(v1)


# Affichage des courbes
plt.title("Suites")
plt.xlabel("n")
plt.plot(n, u, label="u(n)")
plt.plot(n, v, label="v(n)")
plt.legend()

# Nécessaire sur Mac
plt.show()
