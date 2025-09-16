"""
Exercício 3: Filtrando Números Primos 

Sua tarefa é criar um programa que percorra uma lista de números e crie uma nova lista 
contendo apenas os números que forem primos. 
●  Entrada: Uma lista de números inteiros. 
●  Saída: Uma nova lista com os números primos encontrados.

dica: divisao de resto, modulo ou range
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_primos = []

for i in lista:
    eh_primo = True
    if i < 2:
        eh_primo = False
    else:
        for n in range(2, i):
            if i % n == 0:
                eh_primo = False
                break
    if eh_primo:
        lista_primos.append(i)

print(lista)
print(lista_primos)