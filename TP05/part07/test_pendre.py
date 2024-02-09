# -*- coding: utf-8 -*-
"""
@author: Ppt
"""
import random
import matplotlib.pyplot as plt

# lseg est une Liste de 10 listes de coordonnées de 2 points du type [[xA,yA],[xB,yB]] définissant un segment plus un 11ème élément ('tete')
lseg=[[[0,10],[0,0]],[[5,5],[0,20]],[[5,20],[20,20]],[[5,10],[15,20]],[[20,20],[20,16]],[[20,20],[15,7]],[[20,17],[7,3]],[[20,23],[7,3]],[[20,17],[12,12]],[[20,23],[12,12]],'tete']



def lexique(f):
    '''
    Paramètre : fichier f (chaîne de caractères) présent dans le dossier courant contenant un mot par ligne
    Résultat : liste contenant les mots du fichier
    '''
    lex = []
    fichier = open(f, 'r')
    for ligne in fichier:
        lex.append(ligne.strip('\n'))
    fichier.close()
    return lex

def tirer(l):
    '''
    Paramètre : liste l
    Résultat : retourne un élément de la liste l choisi aléatoirement
    '''
    # Je ne sais si vous avez déjà vu cela
    assert type(l) is list, "Le paramètre de 'tirer()' n'est pas une liste."
    assert len(l) > 1, "Le nombre d'éléments de la liste est inférieur à 2."
    n = random.randint(0, len(l)-1)
    return l[n]

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

def masquer(ch):
    """
    Paramètre : Chaîne de caractères ch
    Résultat : liste de '_' en même quantité que le nombre de lettres de ch
        affiche le nombre de lettres que possède la chaîne ch
    """
    assert type(ch) is str, "Le paramètre de masquer n'est pas une chaîne de caractères"
    l=[]
    for c in ch:
        l+='_'
    print('Le mot à trouver avec moins de 10 erreurs possède',len(l),'lettres')
    return l

def afficher(l):
    '''
    Paramètre : liste de caractères l
    Résultat : None. 
    Affiche une chaine de caractères contenant les caractères de la liste avec des espaces
    Par exemple la liste ['d','_','n','_','l','d'] conduit à afficher la chaîne 'd _ n _ l d'        
    '''
    assert type(l) is list, "Le paramèrte de afficher() n'est pas une liste"
    for c in l:
        assert type(c) is str and len(c)==1, "Un des éléments de la liste n'est pas un caractère"
    ch=''
    for e in l:
        ch+=e
    print(ch)

def pendre():
    '''
    Paramètre : aucun
    Résultat : lance le jeu, gère le graphe
               retourne un boléen True ou False selon la réussite ou non de la partie
    '''    
    # Chargement de la liste des mots
    l = lexique("lexique.txt")

    # Tirage du mot à trouver
    mot = tirer(l)

    # Génération du mot masqué
    masque = masquer(mot)
    
    # Affichage du mot masqué 
    afficher(masque)
    
    # Initialisation à 0 du nombre d'échecs
    echecs=0
    
    # Critère d'arrêt
    drapeau = False
    
    # Fermture d'une éventuelle fenêtre existante
    plt.close()

    # Création d'une nouvelle fenêtre graphique
    plt.axis([-5, 30, -5, 25])

    # on démarre la boucle
    while not drapeau and echecs <11:
        ok = False
        while not ok:
            ch = input("Choisir une lettre : ")
            if type(ch) is str and len(ch) == 1 and ch.isalpha() and ch.islower():
                ok = True
            else:
                print("Caractère non valide")
        if mot.find(ch) == -1:
            print("La lettre n'est pas dans le mot à trouver")
            echecs +=1
            tracer(lseg, echecs)
            plt.pause(.2)
        else:
            print("La lettre est dans le mot à trouver")
            # La lettre peut être présente plusieurs fois
            for i in range(0, len(mot)):
                if mot[i] == ch:
                    masque[i] = ch
        afficher (masque)
        fini=True
        for i in range(0,len(masque)):
            if masque[i] == '_':
                fini = False
        if fini == True:
            drapeau = True
    
    if drapeau :
        print("bravo")
        plt.text(5,22, 'BRAVO', c='r')
    else:
        print("pendu")
        plt.text(5, 22, 'PENDU le mot était :' + mot, c='r')
    plt.pause(5)
    return drapeau


    
pendre()
    
    
    
    
    
    
    
    
    
    
    
    # arrivé ici on est sorti de la boucle, soit victorieux soit perdant
    
