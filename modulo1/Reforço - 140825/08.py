# Faça um programa que solicita uma palavra e imprime a quantidade de vogais (a, e, i, o, u) que ela contém.

palavra = (input("Digite uma palavra: ")).lower()
chave = "aeiou"
contador = 0

for letra in palavra:
    if letra in chave:
        contador += 1

print(f"A palavra '{palavra}' contém {contador} vogais.")