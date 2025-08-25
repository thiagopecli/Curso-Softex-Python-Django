"""Crie um programa que solicita ao usuário um número e, em seguida, usa um loop for para 
imprimir todos os números pares de 2 até o número digitado."""

numero = int(input("Digite um número: "))

for i in range(2, numero + 1, 2):
    print(i)