import math

v = int(input("Nombre ? "))
f = 1
for i in range(2, v+1):
    f = f*i
print("Résultat calculé :", f)

f2 = math.factorial(v)
if f == f2:
    print("Le résultat est correct")
else:
    print("Erreur de calcul, il fallait trouver :", f2)
