
def nbmots(liste):
    '''Retourne le nombre d'éléments dans la liste
    Paramètre : liste de mots liste
    Résultat : Nombre de mots
    '''
    # Initialisation du compteur
    n = 0

    # Incrémente le nombre pour chaque élément de la liste
    for mot in liste:
        n += 1

    # Renvoi du résultat
    return n


def pluslongmot(liste):
    '''Retourne la liste des mots les plus longs de la liste d'éntrée
    Paramètre : Liste des mots à analyser liste
    Résultat : Liste des mots les plus longs de la liste en entrée
    '''

    liste_max = list()  # Initialisation de la liste de sortie (vide)
    lg_max = 0  # Initialisation de la longueur max des mots de la liste de sortie

    # Itération sur les mots de la liste d'entrée
    for mot in liste:
        lg_mot = len(mot)  # Calcul de la longueur du mot courant

        # Si la longueur du mot courant est supérieure à la longueur maximale courante,
        # la liste des mots les plus longs est réinitialisée à partir de celui-ci
        if lg_mot > lg_max:
            liste_max = [mot]
            lg_max = lg_mot  # Mise à jour de la longueur maximale
        # Si la longueur du mot courant est égale à la longueur maximale courante,
        # le mot est ajouté à la liste des mots les plus longs
        elif lg_mot == lg_max:
            liste_max.append(mot)
        # Sinon, le mot est ignoré

    # Renvoi de la liste des mots les plus longs
    return liste_max


def isinliste(liste, ch):
    '''Retourne la liste des mots contenant une chaine définie
    Paramètre :  Liste des mots dans lesquels la chaine est à rechercher liste
    Chaine à rechercher ch
    Résultat: Liste des mots contenant la chaine fournie en paramètre
    '''
    l = list()  # Initialisation de la liste des mots contenant la chaine

    # Itération sur la liste des mots
    for mot in liste:
        # Si la chaine est dans le mot, il est ajouté à la liste résultat
        if ch in mot:
            l.append(mot)

    # Renvoi de la liste obtenue
    return l


# Chargement de la liste à partie du fichier
l = list()
# ATTENTION : J'ai dû définir la méthode d'encodage
fichier = open('listemots.txt', 'r', encoding="ISO-8859-1")
for ligne in fichier:
    l.append(ligne.strip('\n'))
fichier.close()

# Affichage du nombre de mots
print('Nombre de mots :', nbmots(l))

# Affichage de la liste des mots les plus longs
print('Mots les plus longs', pluslongmot(l))

# Afichage de la liste des mots contenant la chaine saisie
ch = input('Quelle chaîne voulez-vous chercher ? ')
print(isinliste(l, ch))
