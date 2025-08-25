"""Escreva um programa que pede ao usuário para digitar um nome e um sobrenome. O 
programa deve imprimir o nome completo e a quantidade de caracteres em cada um, 
separadamente."""

# 1. Pede o nome e o sobrenome ao usuário
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

# 2. Cria um dicionário para armazenar os resultados
contagem_caracteres = {}

# 3. Calcula o comprimento de cada string e armazena no dicionário
#    Usamos len() para contar os caracteres de cada variável separadamente.
contagem_caracteres[nome] = len(nome)
contagem_caracteres[sobrenome] = len(sobrenome)

# 4. Exibe os resultados de forma organizada
print("\n--- Resultado da Contagem ---")
# Usamos .items() para percorrer as chaves (palavras) e os valores (contagens)
for palavra, quantidade in contagem_caracteres.items():
    print(f"A palavra '{palavra}' tem {quantidade} caracteres.")