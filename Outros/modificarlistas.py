######## Listas: As Coleções do seu Programa ########

# Metodo para modificar listas

# Metodo .append(item) adiciona novo item no final da lista
lista_presente = ["roupa", "sapato", "brinquedo"]
lista_presente.append("video game")
print(lista_presente)

# Metodo .insert(indice, item) adiciona um item na posição que indicar e empurra o restante dos itens para a direita. 
lista_presente = ["roupa", "sapato", "video game"]
lista_presente.insert(0, "brinquedo")
print(lista_presente)

# Metodo .remove(item) remove a primeira ocorrencia de um item especifico
lista_compras = ["arroz", "feijão", "açúcar", "oleo", "leite"]
lista_compras.remove("oleo")
print(lista_compras)

# Metodo .pop(indice) remove e retorna o item na posição especificada. obs: se não especificar, ele remove e retorna o ultimo item da lista
lista = [10,20,30,40,50]
item_removido = lista.pop(1)
print(f"Lista apos o POP: {lista}")
print(f"Item removido: {item_removido}")

# Metodo .sort() organiza a lista. Para números organiza de forma crescente, para string por ordem alfabetica.

lista = ["miojo", "sabão", "chocolate", "leite", "sazon"]
numeros = [5,2,6,8,9,7,4]
lista.sort()
numeros.sort()
print(lista)
print(numeros)

# Metodo .reverse() inverte a ordem dos elementos da lista, sem ordena-los
lista = ["miojo", "sabão", "chocolate", "leite", "sazon"]
numeros = [5,2,6,8,9,7,4]
lista.reverse()
numeros.reverse()
print(lista)
print(numeros)

# Metodo .index(item) retorna o indice (a posição) da primeira ocorrencia do item especificado. Se o item não for encontrado, ele causa erro.
lista = ["miojo", "sabão", "chocolate", "leite", "sazon"]
posicao_item = lista.index("chocolate")
print(posicao_item)