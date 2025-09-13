"""18. Encontrando Elementos Comuns em Múltiplas Listas: Crie três listas: lista1 = [1, 2, 3, 
4], lista2 = [3, 4, 5, 6], lista3 = [4, 6, 7, 8]. Use conjuntos para encontrar o(s) número(s) 
que aparece(m) nas três listas."""

lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [4, 6, 7, 8]

print(f"Lista 1: {lista1}")
print(f"Lista 1: {lista2}")
print(f"Lista 1: {lista3}")

set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

comun_nas_tres = set1.intersection(set2, set3)
print(f"Números que aparecem nas três listas: {comun_nas_tres}")