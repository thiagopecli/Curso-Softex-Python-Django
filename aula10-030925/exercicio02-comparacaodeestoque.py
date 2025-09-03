estoque_principal = [("Camiseta", 101), ("Calça", 102), ("Boné", 103), ("Tênis", 104)]
estoque_online = [("Boné", 103), ("Camisa Polo", 105), ("Calça", 102), ("Chinelo", 106)]

principal = set(estoque_principal)
online = set(estoque_online)

consolidado = []

consolidado = principal.intersection(online)
print(consolidado)

somente_loja = principal.difference(online)
print(somente_loja)

somente_online = online.difference(principal)
print(somente_online)
