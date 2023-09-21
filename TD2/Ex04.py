# Création de la liste par compréhension
l = [x for x in range(100) if (x % 5 == 0 or x %
                               7 == 0) and not (x % 5 == 0 and x % 7 == 0)]

print(l)
