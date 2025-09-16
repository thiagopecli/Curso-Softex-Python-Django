"""20. Vendas Simples: Crie um dicionário de estoque e outro de vendas. Simule uma venda, 
diminuindo a quantidade no estoque e adicionando a venda ao dicionário de vendas. Use 
if para garantir que há estoque suficiente."""

estoque = {'produto1': 10, 'produto2': 5}
vendas = {}

produto_venda = 'produto1'
quantidade_venda = 3

if estoque.get(produto_venda, 0) >= quantidade_venda:
    estoque[produto_venda] -= quantidade_venda
    vendas[produto_venda] = vendas.get(produto_venda, 0) + quantidade_venda
    print(f"Venda realizada: {quantidade_venda} unidades de {produto_venda}")
else:
    print(f"Estoque insuficiente para {produto_venda}")
print(f"Estoque atual: {estoque}")
print(f"Vendas realizadas: {vendas}")