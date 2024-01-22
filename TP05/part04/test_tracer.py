# -*- coding: utf-8 -*-
"""
@author: Ppt
"""
import matplotlib.pyplot as plt

plt.close()

# lseg est une Liste de 10 listes de coordonnées de 2 points du type [[xA,yA],[xB,yB]] définissant un segment plus un 11ème élément ('tete')
lseg=[[[0,10],[0,0]],[[5,5],[0,20]],[[5,20],[20,20]],[[5,10],[15,20]],[[20,20],[20,16]],[[20,20],[15,7]],[[20,17],[7,3]],[[20,23],[7,3]],[[20,17],[12,12]],[[20,23],[12,12]],'tete']

def tracer(l,i):
    '''
    Paramètres : l liste de listes de coordonnées de couples de points définissant des segments
                 i indice pour repérer le segment à tracer
    Résultats : trace le segment d'indice i-1 sur un graphe déjà existant
                trace une tête si l'indice vaut len(l)
    '''
    assert i>0 and i<=len(l), "Indice demandé incorrect"

    if i <len(l):
        plt.plot(l[i-1][0],l[i-1][1],lw=5,c='k')
    else: # On ajoute la tête si i vaut len(l)
        plt.plot(20,15,marker='o',markersize='30',mec='k')


for i in range(1,12):
    tracer(lseg, i)

# Nécessaire sur mon poste
plt.show()

