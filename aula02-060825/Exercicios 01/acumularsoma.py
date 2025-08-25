# Acumulador de Soma 
# ● Peça ao usuário para digitar 5 números. 
# ● Use um while com um contador para somar todos os números digitados e imprimir o 
# resultado final. 

soma = 0
contador = 0

print("=== Acumulador de Soma ===")
print("Digite 5 números para somar:")

while contador < 5:
    num = int(input(f"Digite o {contador + 1}º número: "))
    soma += num
    contador += 1

print(f"\n=== Resultado ===")
print(f"A soma dos 5 números digitados é: {soma}")
print(f"Total de números digitados: {contador}")
print(f"Total de números digitados: {contador}")