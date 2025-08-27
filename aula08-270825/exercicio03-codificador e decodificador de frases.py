"""
Exercicio 03: Codificador e Decodificador de Frases

Crie um programa que codifica e decodifica uma frase, seguindo as regras abaixo: 
Cada vogal deve ser substituida pelo número correspondente: 

a - 1
e - 2
i - 3
o - 4
u - 5

O programa deve: 

1. Ler uma frase digitada pelo usuário:
2. Exibir a frase codificada, trocando as vogais pelos numeros:
3. Exibir a frase decodificada, voltando os numeros as vogais originais:

"""

frase = input("Digite uma frase para Codificar ou Decodificar: ")

frase_codificada = frase
frase_codificada = frase_codificada.replace("a", "1")
frase_codificada = frase_codificada.replace("e", "2")
frase_codificada = frase_codificada.replace("i", "3")
frase_codificada = frase_codificada.replace("o", "4")
frase_codificada = frase_codificada.replace("u", "5")
print(f"Frase codificada: {frase_codificada}")

frase_decodificada = frase_codificada
frase_decodificada = frase_decodificada.replace("1", "a")
frase_decodificada = frase_decodificada.replace("2", "e")
frase_decodificada = frase_decodificada.replace("3", "i")
frase_decodificada = frase_decodificada.replace("4", "o")
frase_decodificada = frase_decodificada.replace("5", "u")
print(f"Frase Decodificada: {frase_decodificada}")
