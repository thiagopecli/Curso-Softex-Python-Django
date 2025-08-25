# 5. Substituindo palavras
# Peça uma frase e uma palavra para substituir
# Depois peça a nova palavra e use .replace() para fazer a troca

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para substituir: ")
palavra_substituta = input("Digite a palavra nova: ")

frase = frase.replace(palavra, palavra_substituta)
print(f"A nova frase é: {frase}.")