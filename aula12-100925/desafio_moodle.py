vogais = "aeiouáéíóúâêîôûãõ"
consoantes = "bcdfghjklmnpqrstvwxyzç"
contador_vogais = 0
contador_consoantes = 0

frase_usuario = input("Digite a frase: ").lower()
palavras = frase_usuario.split()
quantidade_palavras = len(palavras)

for letra in frase_usuario:
    if letra in vogais:
        contador_vogais += 1
    elif letra in consoantes:
        contador_consoantes += 1

frase_formatada = frase_usuario.replace(' ', '')
frase_invertida = frase_formatada[::-1]
se_e_palindromo = (frase_formatada == frase_invertida)

print(f"Palavras: {quantidade_palavras}")
print(f"Vogais: {contador_vogais}")
print(f"Consoantes: {contador_consoantes}")
print(f"É palindromo? {'Sim' if se_e_palindromo else 'Não'}")