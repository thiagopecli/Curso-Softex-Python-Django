"""
Exercício 2: Encontrando Elementos Comuns 

Você tem duas listas e precisa encontrar os elementos que aparecem em ambas. O programa 
deve gerar uma terceira lista contendo apenas os elementos em comum, sem repetições. 
●  Entrada: Duas listas. 
●  Saída: Uma nova lista com os elementos que as duas listas têm em comum.
"""

lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
lista3 = list(set(lista1) & set(lista2))
print(lista3)

lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
lista3 = []

for i in lista1:
    if i in lista2:
        lista3.append(i)
        print(lista3)