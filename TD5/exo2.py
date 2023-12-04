# -*- coding: utf-8 -*-
"""
Exercice 2 du TD5
"""
import matplotlib.pyplot as plt
import numpy as np

# Fermeture de l'éventuel graphique courant
plt.close()

# Séquence d'acides aminés
sequence = "AGWLWHGAASPSGGASAGLAMPPGAIMPALGWILWIIHGPSAILWIGASAIMPGALW"

# Création du dictionnaire
dico = dict()
for acide in sequence:
    if acide in dico:
        dico[acide] = dico[acide]+1
    else:
        dico[acide] = 1

# Affichage de l'histogramme
plt.bar(dico.keys(), dico.values())

# Libellés pour les axes X et Y
plt.xlabel("Acides aminés")
plt.ylabel("Occurrences")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
