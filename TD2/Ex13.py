l = [1, 2, 4, 6, 10, 12, 26, 1, 6, 10, 1]
n = int(input('Saisir un nombre : '))
nb = len([x for x in l if x == n])
print("Nombre d'occurrences : ", nb)
