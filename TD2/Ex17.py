l = []
for i in range(1, 6):
    fini = False
    while not fini:
        v = int(input('Entrer le numéro '+str(i)+' : '))
        if len(l) == 0:
            l.append(v)
            fini = True
        elif v > l[len(l)-1]:
            l.append(v)
            fini = True
        else:
            print('Nombre trop petit')
print('Liste :', l)
