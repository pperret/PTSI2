# Création de la liste en une ligne avec compréhension
l = [x for x in range(10, 100, 2)]
print(l)

# Création de la ligne en une ligne sans compréhension
l = list(range(10, 100, 2))
print(l)

# Création de la liste en 3 lignes avec une boucle for
l = list()
for x in range(10, 100, 2):
    l.append(x)
print(l)
