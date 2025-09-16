"""19. Análise de Dados: Dada uma lista de dicionários de produtos (com nome e preço), 
encontre e imprima o nome e o preço do produto mais caro."""

produtos = [
    {"nome": "Produto A", "preco": 50},
    {"nome": "Produto B", "preco": 75},
    {"nome": "Produto C", "preco": 100}
]
produto_mais_caro = max(produtos, key=lambda x: x["preco"])
print(f"Produto mais caro: {produto_mais_caro['nome']} - Preço: {produto_mais_caro['preco']}")