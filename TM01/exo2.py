# Saisie du nombre d'étage
nb_etages = int(input("Nombre d'étages : "))

# Cumul du nombre de cubes (initialisé avec la valeur correspondant au premier étage)
nb_cubes = 1

# Boucle sur le nombre d'étages (sauf le premier)
for i in range(1, nb_etages):
    # Ajout du nombre de cubes de l'étage considéré
    nb_cubes = nb_cubes + (i*2+1)**3

# Affichage du résultat (nombre total de cubes)
print('Nombre total de cubes :', nb_cubes)
