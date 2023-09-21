l1 = [4, 8, 7, 12]
l2 = [3, 6]

# Utilisation d'une liste intermédiaire et de la fonction sum
l = []
for i1 in l1:
    for i2 in l2:
        l.append(i1*i2)
s = sum(l)
print(s)

# Autre méthode sans liste intermédiaire (plus efficace)
s = 0
for i1 in l1:
    for i2 in l2:
        s = s+i1*i2
print(s)
