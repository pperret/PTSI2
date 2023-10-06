def f(t):
    r=0
    for x in t:
    r *= x
    return (r)

# 1) Il faut que t soit une liste
# 2) Ca ressemble à la multiplication entre eux des éléments d'une liste sauf que:
#     - r devrait initialisé à 1 (autrement, le résultat est toujours)
#     - Il faudrait indenter 'r *= x' pour que ce soit dans la boucle du for
#     - De plus, les parenthèses dans le return sont inutiles
