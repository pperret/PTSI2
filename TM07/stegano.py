#!/usr/bin/python3
# Programme d'extraction et d'affichage d'une image cachée dans une autre
# En modifiant légèrement le programme, il est possible de restreinte le fonctionnement
# soit à l'extraction uniquement, soit à l'affichage uniquement.

import matplotlib.pyplot as plt
import numpy as np

# Fermeture des éventuelles fenêtres existantes
plt.close()

# Lecture du fichier d'entrée
tab = plt.imread('ptsi2.bmp')

# Récupération des dimensions du tableau contennat l'image
lig, col, cou = tab.shape

# Création d'un tableau de dimension identiques pour le résultat
tab2 = np.zeros((lig, col, cou), dtype='uint8')

# Extraction de l'image cachée

# Version basique
# for i in range (0,lig):
#    for j in range (0,col):
#        for k in range(0,cou):
#            tab2[i][j][k] = (tab[i][j][k] %16) * 16

# Version en utilisant les fonctionalités numpy
tab2 = (tab % 16)*16

# Sauvegarde de l'image (dans un autre fichier)
plt.imsave('ptsi2_res.bmp', tab2)

# Affichage de l'image résultante
plt.imshow(tab2)

# Nécessaire sur mon PC
plt.show()
