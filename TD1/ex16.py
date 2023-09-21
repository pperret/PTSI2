import math

n = int(input("Saisir n : "))
x = float(input("Saisir x : "))
s = 0
for k in range(0, n+1):
    s = s + x**k/math.factorial(k)
print("Résultat calculé :", s)
print("Résultat théorique :", math.exp(x))
