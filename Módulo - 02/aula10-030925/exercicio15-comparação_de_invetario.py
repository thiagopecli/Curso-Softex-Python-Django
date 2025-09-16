"""Nível Avançado (Exercícios 15 a 20)  
15. Comparação de Inventário: Você tem uma tupla de itens do seu estoque estoque = 
('camisa', 'calça', 'sapato') e uma lista de itens que foram vendidos vendidos = ['camisa', 
'meia', 'calça']. Use conjuntos para encontrar os itens que foram vendidos mas ainda 
estão no estoque. """

estoque = ('camisa', 'calça', 'sapato')
vendidos = ['camisa', 'meia', 'calça']
print(f"Produtos do estoque(Tuplas): {estoque}")
print(f"Produtos vendidos(Listas): {vendidos}")

set_estoque = set(estoque)
set_vendidos = set(vendidos)
itens_em_comum = set_estoque.intersection(set_vendidos)

print(f"Itens vendidos que estavam em estoque: {itens_em_comum}")