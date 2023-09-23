# Cumul du nombre de grains de blé
nb_grains = 0

# Boucle sur les cases de l'échiquier
for i in range(0, 64):
    nb_grains = nb_grains + 2**i

# Calcul du nombre de micromoles
nb_micro_moles = nb_grains/6.02E23*1E6

# Affichage du résultat
print('Nombre de micromoles de grains de blé :', nb_micro_moles)
