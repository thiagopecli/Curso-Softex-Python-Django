# 3. Listas e Indexação:

# Dada a lista de numeros [10, 20, 30, 40, 50], faça:
#   Acesse e imprima o terceiro elemento;
#   Adicione o número 60 no final da lista;
#   Remova o número 20 da lista.

lista = [10, 20, 30, 40, 50]

print(lista[2]) # Acessando o terceiro elemento.

lista.append(60) # Adicionando o número 60 no final da lista.
print(lista) # Imprimindo a lista com o elemento 60.

lista.remove(20) # Removendo o número 20 da lista.
print(lista) # Imprimindo a lista SEM o elemento 20.