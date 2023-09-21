r1 = float(input("Entrer le premier réel : "))
r2 = float(input("Entrer le second réel : "))
if r1 == 0 or r2 == 0:
    print("Résultat nul")
else:
    f1 = r1 >= 0
    f2 = r2 >= 0
    if (f1 and f2) or (not f1 and not f2):
        print("Résultat positif")
    else:
        print("Résultat négatif")
