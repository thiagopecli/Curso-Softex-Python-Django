# Desenho de Triangulo: Crie um programa que solicita um numero ao usuario. Use um loop for aninhado para imprimir um triangulo retangulo de asteristicos, com a altura correspondente ao numero digitado.

altura = int(input("Digite a altura do triangulo: "))

for i in range(1, altura + 1):
    print("*" * i)