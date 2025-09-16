# Contador Regressivo 
# ● Peça um número inteiro ao usuário. 
# ● Use um while para fazer uma contagem regressiva a partir desse número até 0. Imprima 
# cada número. 

num = int(input("Digite um número inteiro para iniciar a contagem regressiva: "))
print(f"Contagem regressiva a partir do número: {num}")
while num > 0:
    print(num)
    num -= 1
print("Contagem regressiva finalizada!")
print("Chegou a zero!")