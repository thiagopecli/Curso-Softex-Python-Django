lista = [1,3,5]
lista2 = [2,4,6]
lista_combinada = []
inicio = 0
final = 0

while inicio < len(lista) and final < len(lista2):
    if lista[inicio] < lista2[final]:
        lista_combinada.append(lista[inicio])
        inicio += 1
    else:
        lista_combinada.append(lista2[final])
        final += 1

lista_combinada.extend(lista[inicio:])
lista_combinada.extend(lista2[final:])

print(f"\nLista combinada e ordenada: {lista_combinada}.")