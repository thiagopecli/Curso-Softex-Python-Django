# Contador de caracteres e verificador de letras
# Peça uma palavra e mostre
# Quantos caracteres ela tem (len())
# Se "a" está nela

palavra = input("Digite uma palavra: ")
print("A palavra tem", len(palavra), "caracteres.")
if "a" in palavra:
    print("A letra 'a' está na palavra.")
else:
    print("A letra 'a' não está na palavra.")