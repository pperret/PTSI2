# Création de la liste par compréhension
l = [x**2 for x in range(31) if x**2 >= 245]
print(l)

# Création de la liste par une boucle for
l = []
for x in range(31):
    s = x**2
    if s >= 245:
        l.append(s)
print(l)
