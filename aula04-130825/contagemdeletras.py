# 6. Contagem de letras especificas
# Peça um texto e uma letra
# Mostre quantas vezes essa letra aparece usando .count()

texto = input("Digite um texto: ")
letra = input("Digite uma letra: ")
contagem = texto.count(letra)

print(f"A letra '{letra}' aparece {contagem} vezes no texto.")