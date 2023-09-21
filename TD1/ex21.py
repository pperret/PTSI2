sumSquare = 0
sum = 0
for n in range(1, 101):
    sumSquare = sumSquare + n**2
    sum = sum+n
print("Résultat :", sum**2-sumSquare)
