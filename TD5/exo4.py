# -*- coding: utf-8 -*-
"""
Exercice 4 du TD5
"""
import matplotlib.pyplot as plt

plt.close()

# =============================================================================
# Liste des élèves
# =============================================================================
data = []
# ATTENTION : Il faut définir l'encodage sur Mac
fichier = open('PTSI2.txt', 'r', encoding="ISO-8859-1")
for ligne in fichier:
    data.append(ligne.strip('\n').split('\t'))
fichier.close()

# =============================================================================
# Liste des vraies dates du passage du soleil dans les constellations
# =============================================================================
zd = []  # zodiaque dates
# ATTENTION : Il faut définir l'encodage sur Mac
fichier = open('zdates.txt', 'r', encoding="ISO-8859-1")
for ligne in fichier:
    zd.append(ligne.strip('\n').split('\t'))
fichier.close()

# =============================================================================
# Création des dictionnaires d{Nom:Date naissance} et dzd{Zodiaque:Dates}
# =============================================================================
d = dict()
for (nom, date) in data:
    d[nom] = date

dzd = dict()
for (signe, dates) in zd:
    dzd[signe] = dates

# =============================================================================
# Comparaison des dates : ch1 est-elle inférieure ou égale à la ch2
# =============================================================================


def comp(ch1, ch2):
    '''    
    Parameters
    ----------
    ch1 : TYPE str
        Date au format jour/mois. Par exemple 10/03.
    ch2 : TYPE str
        Idem ch1.
    Returns
    -------
    TYPE Booléen
        Renvoie True si ch1 est inférieure ou égale à ch2, False sinon.
    '''

    # Utilisation du slicing pour extraire le jour et mois des dates
    # et conversion sous la forme d'entiers
    jour1 = int(ch1[:2])
    mois1 = int(ch1[3:])
    jour2 = int(ch2[:2])
    mois2 = int(ch2[3:])

    # Comparaison des dates
    if mois1 < mois2:
        return True
    elif mois1 == mois2 and jour1 <= jour2:
        return True
    else:
        return False

# =============================================================================
# Création du dictionnaire dnez{Nom eleve:Zodiaque}
# =============================================================================


# Création du dictionnaire
dnez = dict()

# Boucle sur la liste des élèves
for nom, date in d.items():
    # Boucle sur la liste des signes du zodiaque
    for signe, dates in dzd.items():
        debut = dates[:5]
        fin = dates[6:]
        if comp(debut, date) and comp(date, fin):
            dnez[nom] = signe
        # Cas particulier pour le sagittaire qui est à cheval sur deux années
        # Pour l'identifier, c'est celui dont la date de fin est avant celle de début
        elif comp(fin, debut) and (comp(debut, date) or comp(date, fin)):
            dnez[nom] = signe

# =============================================================================
# Pour faire l'histogramme de la classe : dhis{Signe du zodiaque:Occurrences}
# =============================================================================

#  Création du dictionnaire
dhis = dict()

# Initialisation de chaque signe dans le nouveau dictionnaire
# (y compris ceux qui n'ont potentiellement pas d'élèves)
for k in dzd.keys():
    dhis[k] = 0

# Enumération des valeurs (signe de chaque élève) du dictionnaire contenant le
# signe de chaque élève afin d'incrémenter le compteur du signe correspondant
for signe in dnez.values():
    dhis[signe] = dhis[signe] + 1

# =============================================================================
# Affichage de l'histogramme
# =============================================================================
# Il faut forcer la taille des labels des barres car autrement, il y a du chevauchement
plt.rc('xtick', labelsize=4)

# Affichage de l'histogramme
plt.bar(dhis.keys(), dhis.values())

# Libellés pour les axes X et Y
plt.xlabel("Signes du zodiaque")
plt.ylabel("Occurrences")
plt.legend()

# ATTENTION : Nécessaire sur MAC
plt.show()
