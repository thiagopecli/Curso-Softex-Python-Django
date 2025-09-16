# Escreva um programa que solicita ao usuario para digitar cinco numeros, um de cada vez. Use o loop for para coletar os cinco numeros e, com condicionais, encontre e imprima o maior numero entre eles.

num_maior = None

for i in range(5):
    num = int(input("Digite um número: "))
    if num_maior is None or num > num_maior:
        num_maior = num

print(f"O maior número digitado foi {num_maior}.")