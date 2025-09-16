# A Função range() gera uma sequência de números, que pode ser usada para iterar um número específico de vezes.
# range(10): cria uma sequencia de números de 0 a 9, o 10 não é incluso.
for numero in range(10):
    print(f"Este é o número {numero}")

# range(10, 20): cria uma sequência de números de 10 a 19, o 20 não é incluso.
for numero in range(10, 20):
    print(f"Este é o número {numero}")

# range(10, 20, 2): cria uma sequência de números de 10 a 19, pulando de 2 em 2.
for numero in range(10, 20, 2):
    print(f"Este é o número {numero}")