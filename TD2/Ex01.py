
notes = []
for i in range(1, 6):
    note = float(input('Saisir la note n°' + str(i) + ' : '))
    notes.append(note)
moyenne = sum(notes)/len(notes)
print('La moyenne est :', moyenne)
