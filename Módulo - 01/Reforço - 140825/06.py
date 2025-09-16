# Escreva um programa que solicita uma palavra e verifica se ela tem a letra 'x'. 

palavra = input("Escreva uma palavra: ")
conversor_palavra = palavra.lower()
chave = "x"

if chave in conversor_palavra:
    print(f"Esta palavra '{palavra}' tem a letra 'x'.")
else: 
    print(f"Esta palavra '{palavra}' não contém a letra 'x'.")