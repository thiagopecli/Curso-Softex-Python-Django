# Contador de vogais: Faça um programa que pede ao usuario para digitar uma palavra. Use um loop for para percorrer a palavra e contar quantas vogais (a,e,i,8,u) ela possui. O programa deve desconsiderar maiuscula e minusculas.

palavra = input("Digite uma palavra: ")
contador = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        contador += 1

print(f"A palavra '{palavra}' possui {contador} vogais.")