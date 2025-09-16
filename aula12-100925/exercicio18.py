"""18. Filtro de Lista com lambda: Crie uma função que receba uma lista de números e use 
um loop para retornar uma nova lista apenas com os números pares. Use uma lambda 
dentro do loop. Imprima o resultado."""

def filtrar_pares(numeros: list) -> list:
    pares = []
    for n in numeros:
        if (lambda x: x % 2 == 0)(n):
            pares.append(n)
    return pares

resultado = filtrar_pares([1, 2, 3, 4, 5, 6])
print(f"Números pares: {resultado}")