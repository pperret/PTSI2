# Suite de Fibonacci généralisée (i.e. les deux premières valeurs ne sont pas 0 et 1)
suite = [2, 2]
for i in range(2, 50):
    suite.append(suite[i-1]+suite[i-2])
print(suite)
