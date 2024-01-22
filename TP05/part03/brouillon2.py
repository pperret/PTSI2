# -*- coding: utf-8 -*-
"""
@author: Ppt
"""
import matplotlib.pyplot as plt

plt.close()

# lseg est une Liste de 10 listes de coordonnées de 2 points du type [[xA,yA],[xB,yB]] définissant un segment plus un 11ème élément ('tete')
lseg=[[[0,10],[0,0]],[[5,5],[0,20]],[[5,20],[20,20]],[[5,10],[15,20]],[[20,20],[20,16]],[[20,20],[15,7]],[[20,17],[7,3]],[[20,23],[7,3]],[[20,17],[12,12]],[[20,23],[12,12]],'tete']


for i in range(0,10):
    plt.plot(lseg[i][0], lseg[i][1])

# Nécessaire sur mon poste
plt.show()
