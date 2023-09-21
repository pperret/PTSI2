ok = False
while not ok:
    v = float(input("Saisir un nombre entre -10 et 10 : "))
    if v > 10:
        print("Trop grand")
    elif v < -10:
        print("Trop petit")
    else:
        print("Nombre valide")
        ok = True
