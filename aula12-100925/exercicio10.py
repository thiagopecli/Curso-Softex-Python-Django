"""10. Contador de Vogais: Crie uma função que receba uma string e retorne o número de 
vogais (a, e, i, o, u) que ela contém. Imprima o resultado."""

def contar_vogais(texto: str) -> int:
    vogais = "aeiou"
    contador = 0
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    return contador

resultado = contar_vogais("Olá, mundo!")
print(f"O número de vogais é: {resultado}")