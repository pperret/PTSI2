l = [1, 2, 3, 10, 6, 12]
l.sort()

# Méthode avec énumération
ok = True
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        ok = False
if ok:
    print('La liste est triée')
else:
    print("La liste n'est pas dans l'ordre")

# Autre méthode en comparant avec la liste triée
if l == sorted(l):
    print('La liste est triée')
else:
    print("La liste n'est pas dans l'ordre")
