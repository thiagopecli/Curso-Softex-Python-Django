# Somador de Números Positivos 
# ● Use um while True para pedir números ao usuário. 
# ● Some todos os números positivos. 
# ● Se o usuário digitar um número negativo, use break para sair do loop e imprima a soma total. 

soma = 0

print("=== Somador de Números Positivos ===")
print("Digite números positivos para somar (digite um número negativo para encerrar):")
while True:
    num = float(input("Digite um número: "))    
    if num < 0:
        break
    soma += num

print(f"\n=== Resultado ===")
print(f"A soma dos números positivos digitados é: {soma}")