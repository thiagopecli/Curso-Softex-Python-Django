vendas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Fone", 45, 1), ("WebCam", 75.20, 2)]

produto_unico = set()
vendas_filtradas = []

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        vendas_filtradas.append((produto, valor, quantidade))
    
    produto_unico.add(produto)

print(f"Vendas Filtradas valor total 100: {vendas_filtradas}")
print(f"produtos unicos: {produto_unico}")