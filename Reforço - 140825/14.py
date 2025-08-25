"""Faça um programa que solicita um número inteiro e calcula o seu fatorial (ex: 5! = 120). Use 
um loop for."""

num = int(input("Digite um número: "))

if num < 0:
    print("Erro! Número não fatorial.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1

for i in range(1, num + 1):
    fatorial = fatorial * i

print(f"O fatorial de {num} (ou {num}!) é {fatorial}.")
