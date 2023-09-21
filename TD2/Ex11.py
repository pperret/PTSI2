import math

notes = []

# Saisie de la liste des notes
fini = False
while not fini:
    note = float(input('Saisir une note : '))
    if note == 99:
        fini = True
    else:
        notes.append(note)

# Calcul des différentes valeurs
moyenne = sum(notes)/len(notes)
meilleure = max(notes)
nb_au_dessus = len([x for x in notes if x > moyenne])
ecart_type = math.sqrt(sum([((x-moyenne)**2) for x in notes])/(len(notes)-1))

# Affichage des résultats
print('Moyenne : ', moyenne)
print('Meilleure note : ', meilleure)
print('Nombre de notes au-dessus de la moyenne : ', nb_au_dessus)
print('Ecart type : ', ecart_type)
