# Palavra proibida
# Peça uma frase e verifique se a palavra "bomba" aparece nela.

frase = input("Digite uma frase: ")
if "bomba" in frase:
    print(f"A palavra 'bomba' está na frase.")
else:
    print(f"A palavra 'bomba' não está na frase.")