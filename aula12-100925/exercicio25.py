"""25. Analisador de Texto: Crie uma função que receba um texto e retorne um dicionário 
contendo a contagem de palavras, a contagem de vogais e a contagem de consoantes. Imprima o resultado."""

def analisar_texto(texto: str) -> dict:
    palavras = texto.split()
    contagem_vogais = 0
    contagem_consoantes = 0
    for char in texto.lower():
        if char in "aeiou":
            contagem_vogais += 1
        elif char.isalpha() and char not in "aeiou":
            contagem_consoantes += 1
    return {
        "contagem de palavras": len(palavras),
        "contagem de vogais": contagem_vogais,
        "contagem de consoantes": contagem_consoantes
    }

texto = "Exemplo de texto para análise."
resultado = analisar_texto(texto)
print("Resultado da Análise:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
