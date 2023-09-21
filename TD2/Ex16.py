l = [0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1]

pos = 0  # Index courant dans la liste
max0 = 0  # Longueur de la suite de 0 la plus grande
pos0 = -1  # Position de la suite de 0 la plus grande

# Tant qu'il est possible de trouver une chaine de 0 plus grande
while pos+max0 < len(l):
    reste = l[pos:]  # Reste à analyser
    if reste.count(0) == 0:  # Si plus de 0 jusqu'à la fin de la liste
        pos = len(l)
    else:
        idx0 = reste.index(0)
        reste = l[pos+idx0:]
        if reste.count(1) == 0:  # Si plus de 1 jusqu'à la fin de la liste
            l0 = len(reste)
        else:
            l0 = reste.index(1)
        # Si la nouvelle suite de 0 trouvée est plus grande que les précédentes
        if l0 > max0:
            max0 = l0
            pos0 = idx0+pos
        pos = pos+idx0+l0

# Affichage du résultat
print('Index : ', pos0, ', longueur maximale : ', max0)
