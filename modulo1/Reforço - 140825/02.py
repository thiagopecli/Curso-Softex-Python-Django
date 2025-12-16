# Escreva um programa que pede ao usuario dois números e verifica se a multiplicação deles é igual a 100.

num1 = int(input("Digite o número: "))
num2 = int(input("Digite o número: "))

multiplicacao = num1 * num2
print(f"O Resultado da multiplicação: {multiplicacao}")

if multiplicacao == 100:
    print("O resultado da multiplicação é igual a 100.")
else:
    print("O resultado da multiplicação não é igual a 100.")