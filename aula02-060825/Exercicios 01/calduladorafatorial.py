# Calculadora de Fatorial
# ● Peça um número n ao usuário.
# ● Use um while para calcular o fatorial de n (por exemplo, 5! = 5 * 4 * 3 * 2 * 1).
# ● Imprima o resultado.

n = int(input("Digite um número: "))
fatorial = 1
contador = n

while contador > 0:
    fatorial *= contador
    contador -= 1

print("O fatorial de", n, "é", fatorial)