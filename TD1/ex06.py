nature = input("Nature du montage ? ")
if nature != "s" and nature != "p":
    print("Nature de montage invalide")
else:
    r1 = float(input("Valeur de la première résistance ? "))
    r2 = float(input("Valeur de la seconde résistance ? "))
    if nature == "s":
        r = r1+r2
    else:
        r = 1/(1/r1+1/r2)
    print("La résistance équivalente est :", r)
