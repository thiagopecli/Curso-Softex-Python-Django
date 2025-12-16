"""Escreva um programa que pede ao usuário para digitar uma frase e, em seguida, remove 
todos os espaços em branco, imprimindo a frase modificada e o seu novo comprimento."""

frase = input("Dgigite uma frase: ")
frase_formatada = frase.replace(" ", "")

print(frase_formatada)