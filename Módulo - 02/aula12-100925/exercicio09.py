"""9.  Encontrar o Maior Número: Crie uma função que receba uma lista de números e 
retorne o maior número da lista. Use um loop. Se a lista estiver vazia, retorne None."""

def encontrar_maior(lista):
    if not lista:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

resultado = encontrar_maior([3, 5, 2, 8, 1])
print(f"O maior número é: {resultado}")