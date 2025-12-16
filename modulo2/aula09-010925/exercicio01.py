"""
Exercício 1: Contando Ocorrências 

Crie um programa que conte quantas vezes um número específico aparece em uma lista. 
● Entrada: Uma lista de números e um número para ser procurado. 
● Saída: Um número inteiro que representa a quantidade de vezes que o número 
procurado aparece na lista. 

"""

lista = [2,5,9,2,3,2,1,6,5,4,2,8]
print(lista.count(2))

lista2 = ["casa", "roupa", "rosa", "casa"]
print(lista2.count("casa"))

lista3 = [1,2,3,1,5,6,4,8,6,3,2,8,4,3,1,6,8]
lista3 = lista3.count(8)
print(lista3)

lista4 = [2.2,5.2,2,2.2]
print(lista4.count(2.2))

lista5 = [2.2,5.2,2,2.2,"casa", "roupa", 2,3,1,5,6,4, "rosa", "casa"]
print(lista5.count(2))