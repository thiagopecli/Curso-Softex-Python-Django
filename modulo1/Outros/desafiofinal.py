# 10. Desafio final:

# Crie um dicionário estoque com: 
#   "Maçã": 10
#   "banana": 5
#   "laranja": 8

# Faça o seguinte: 
#   Adicione "pera" com quantidade 12
#   Remova "banana"
#   Imprima apenas os nomes dos itens(chaves)

estoque = {
    "maçã": 10,
    "banana": 5,
    "laranja": 8
}

estoque["pera"] = 12 # Adicionando "pera" com quantidade 12.
del estoque["banana"] # Removendo "banana".
print(estoque.keys()) # Imprimindo apenas os nomes dos itens(chaves).