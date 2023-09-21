# Première partie
l = []
for n in range(4):
    if n % 3 != 0 and n % 2 == 0:
        l.append('Sup'+str(n))
print(l)

# Seconde partie
l1, l2, x = [], [], ['Tombouctou', 'Saint-Etienne', 'Tegucigalpa', 'Tananarive']
for ville in x:
    if ville[0] == 'T':
        l1.append(ville)
    elif ville[1] == 'a':
        l2.append(ville)
print(l1)
print(l2)
