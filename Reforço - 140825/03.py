# Escreva um programa que pede ao usuario para digitar uma cor. O programa deve verificar
# Se a cor é "vermelho", "azul" ou "amarelo", e imprimir "Cor primário!", se a condição for verdadeira.

cor = input("Digite uma cor: ")
primaria = ["vermelho", "azul", "amarelo"]

if cor in primaria:
    print("Esta cor é primária!")
else:
    print("Essa cor não é primária!")