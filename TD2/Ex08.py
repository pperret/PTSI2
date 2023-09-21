l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

# Création de la liste par compréhension
l = [l1[i]+l2[i] for i in range(len(l1))]
print(l)

# Autre méthode (non demandée) : Création de la liste par une boucle for
l = []
for i in range(len(l1)):
    l.append(l1[i]+l2[i])
print(l)
