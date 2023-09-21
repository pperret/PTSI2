# Création de la liste par compréhension
l = [x for x in range(100) if x % 5 == 0 or x % 7 == 0]
print(l)

# Création de la liste par un boucle for
l = []
for x in range(100):
    if x % 5 == 0 or x % 7 == 0:
        l.append(x)
print(l)
