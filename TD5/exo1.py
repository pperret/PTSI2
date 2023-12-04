# -*- coding: utf-8 -*-
"""
Exercice 1 du TD5
"""

d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

# 1 - Mise à jour du prénom
d['prenom'] = 'Jacques'

# 2 - Affichage des clés
for k in d.keys():
    print(k)

# 3 - Affichage des valeurs
for v in d.values():
    print(v)

# 4 - Affichage des couples clé/valeur
for k, v in d.items():
    print(k, v)

# 5 - Stockages des clés/valeurs dans des listes

k = d.keys()
v = d.values()

# 6 Affichage de la phrase demandée
print(d['prenom'], d['nom'], "a", d['age'], "ans")
