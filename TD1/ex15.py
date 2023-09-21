import math

a = float(input("Saisir a : "))
b = float(input("Saisir b : "))
c = float(input("Saisir c : "))

if a == 0:
    r = -c/b
    print("Résultat :", r)
else:
    d = b**2-4*a*c
    if d < 0:
        print("Pas de racine réelle")
    elif d == 0:
        r = -b/(2*a)
        print("Une racine double :", r)
    else:
        r1 = (-b+math.sqrt(d))/(2*a)
        r2 = (-b-math.sqrt(d))/(2*a)
        print("Deux racines : ", r1, "et", r2)
