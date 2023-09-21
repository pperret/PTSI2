max = 0
i = 0
while i < 10:
    v = int(input("Saisir un entier naturel : "))
    if v == 0:
        i = 10
    else:
        if v > max:
            max = v
        i = i+1
print(max)
