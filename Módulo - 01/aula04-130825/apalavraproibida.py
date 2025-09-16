# 9. A palavra proibida com while:
# Enquanto o usuario digitar algo que contenha a palavra "spoiler", deve ser solicitado que digite novamente.

while True:
    frase = input("Digite uma frase: ")
    frase.lower()

    if "spoiler" in frase:
        print(f"A frase '{frase}' contém a palavra 'spoiler', digite novamente. ")
        continue
    else: 
        print("Palavra aceita.")
        break
