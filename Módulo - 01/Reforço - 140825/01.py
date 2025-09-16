# Crie um programa que pede ao usuario para digitar sua idade. 
# Se a idade for maior ou igual a 18, imprima "Você é maior de idade"
# Caso contrário, imprima "Você é menor de idade".

print("\n*** Classificador de idade ***")

idade = input("Digite sua idade: ")

if idade >= "18":
    print(f"Você tem {idade} anos, você é maior de idade!")
else:
    print(f"Você tem {idade} anos, você é menor de idade!")