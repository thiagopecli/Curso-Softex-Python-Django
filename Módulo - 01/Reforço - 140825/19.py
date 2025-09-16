"""Faça um programa que pede ao usuário para digitar 5 números. O programa deve somar 
apenas os números que são positivos. Use um loop for."""

contador = 0

for i in range(5):
    print("\nSomador de números positivos!")
    num = int(input("Digite um número: "))
    if num > 0:
        contador += num
        print(f"Número {num} é positivo e foi somado.")
    else:
        print(f"Número {num} não é positivo e foi ignorado.")
print(f"\nA soma de todos os números positivos foi: {contador}")