"""Nível 3: Integração com Outras Estruturas (Exercícios 11-15) 
 
11. Crie uma lista de dicionários, onde cada dicionário representa um filme com "título" e 
"ano". Imprima o ano do segundo filme da lista."""

filmes = [
    {"título": "Inception", "ano": 2010},
    {"título": "Interstellar", "ano": 2014},
    {"título": "Dunkirk", "ano": 2017}
]

print(f"Ano do segundo filme: {filmes[1]['ano']}")