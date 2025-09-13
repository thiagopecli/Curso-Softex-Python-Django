"""19. Análise de Dados de Vendas: Você tem uma lista de vendas, onde cada venda é uma 
tupla (produto, valor). 
vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)] 
Calcule o valor total de vendas. Em seguida, use um conjunto para contar quantos tipos 
de produtos diferentes foram vendidos."""

vendas = [('teclado', 150), ('mouse', 80), ('teclado', 150)] 
print(f"Registros de vendas: {vendas}")

valor_total = sum(venda[1] for venda in vendas)
print(f"Valor total das vendas: R$ {valor_total:.2f}")

produtos_unicos = {venda[0] for venda in vendas}
quantidade_de_produtos_unicos = len(produtos_unicos)
print(f"Tipos de produtos diferentes vendidos: {quantidade_de_produtos_unicos}")