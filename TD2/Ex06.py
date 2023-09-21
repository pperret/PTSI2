physique = 'physique'
mathematique = 'mathématique'

# Création de la liste par compréhension
l = [x for x in physique if mathematique.count(x) == 0]
print(l)

#  Création de la liste avec une boucle for
l = []
for x in physique:
    if mathematique.count(x) == 0:
        l.append(x)
print(l)
