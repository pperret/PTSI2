annee = int(input("Saisir une année : "))
if (annee % 400 == 0) or (annee % 4 == 0 and annee % 100 != 0):
    print("Année bisextile")
else:
    print("Année non bisextile")
