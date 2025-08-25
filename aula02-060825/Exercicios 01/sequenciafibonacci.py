# Sequência de Fibonacci 
# ● Peça um número n ao usuário. 
# ● Use um while para gerar e imprimir os primeiros n termos da sequência de Fibonacci (0, 
# 1, 1, 2, 3, 5, ...). 

n = int(input("Digite a quantidade de termos da sequência de Fibonacci que deseja ver: "))

a, b = 0, 1
contador = 0
print("=== Sequência de Fibonacci ===")
while contador < n:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1
print()  # Para pular uma linha após a sequência
print(f"\nOs primeiros {n} termos da sequência de Fibonacci foram exibidos.")
