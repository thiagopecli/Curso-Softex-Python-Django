"""19. Ordenador de Dicionários com lambda: Crie uma função que receba uma lista de 
dicionários (cada um com "nome" e "idade"). Use uma lambda e um loop para ordenar a 
lista pela idade e retornar a lista ordenada. Imprima o resultado."""

def ordenar_por_idade(pessoas: list) -> list:
    return sorted(pessoas, key=lambda x: x["idade"])

lista_pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Charlie", "idade": 35}
]

resultado = ordenar_por_idade(lista_pessoas)
print(f"Lista ordenada por idade: {resultado}")
