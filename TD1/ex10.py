v1 = int(input("Saisir le premier entier : "))
v2 = int(input("Saisir le second entier : "))

if v2 > v1:
    v1, v2 = v2, v1

while v1 != 0:
    while v1 >= v2:
        v1 = v1-v2
    if v1 != 0:
        v1, v2 = v2, v1
print("pgcd :", v2)
