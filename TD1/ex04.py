t = float(input("Température de l'eau ? "))
if t >= 100:
    print("Etat gazeux")
elif t > 0:
    print("Etat liquide")
else:
    print("Etat solide")
