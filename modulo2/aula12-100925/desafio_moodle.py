vogais = "aeiouáéíóúâêîôûãõ"
consoantes = "bcdfghjklmnpqrstvwxyzç"

def contar_vogais(frase):
    total_vogais = 0
    for letra in frase:
        if letra in vogais:
            total_vogais += 1
    return total_vogais

def contar_consoantes(frase):
    total_consoantes = 0
    for letra in frase:
        if letra in consoantes:
            total_consoantes += 1
    return total_consoantes

def contar_palavras(frase):
    frase = frase.strip()
    if frase:
        lista_palavras = frase.split()
        return len(lista_palavras)
    else:
        return 0

def eh_palindromo(frase):
    frase_formatada = ''.join(frase.split())
    invertida = frase_formatada[::-1]
    if frase_formatada == invertida:
        return True
    else:
        return False

def analisar_frase(frase):
    frase = frase.lower()
    num_palavras = contar_palavras(frase)
    num_vogais = contar_vogais(frase)
    num_consoantes = contar_consoantes(frase)
    print(f"Palavras: {num_palavras}")
    print(f"Vogais: {num_vogais}")
    print(f"Consoantes: {num_consoantes}")
    if eh_palindromo(frase):
        print("É palindromo? Sim")
    else:
        print("É palindromo? Não")

frase_usuario = input("Digite a frase: ")
analisar_frase(frase_usuario)


# vogais = "aeiouáéíóúâêîôûãõ"
# consoantes = "bcdfghjklmnpqrstvwxyzç"
# contador_vogais = 0
# contador_consoantes = 0
# frase_usuario = input("Digite a frase: ").lower()
# palavras = frase_usuario.split()
# quantidade_palavras = len(palavras)
# for letra in frase_usuario:
#     if letra in vogais:
#         contador_vogais += 1
#     elif letra in consoantes:
#         contador_consoantes += 1
# frase_formatada = frase_usuario.replace(' ', '')
# frase_invertida = frase_formatada[::-1]
# se_e_palindromo = (frase_formatada == frase_invertida)
# print(f"Palavras: {quantidade_palavras}")
# print(f"Vogais: {contador_vogais}")
# print(f"Consoantes: {contador_consoantes}")
# print(f"É palindromo? {'Sim' if se_e_palindromo else 'Não'}")