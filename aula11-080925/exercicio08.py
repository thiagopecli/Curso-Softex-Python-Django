"""8.  Crie um dicionário com produtos e preços. Peça ao usuário para digitar um produto para 
remover. Remova-o do dicionário e imprima o dicionário final. Use if para verificar se o 
produto existe antes de remover."""

produtos = {
    "cadeira": 100,
    "mesa": 200,
    "quadro": 150
}

produto = input("Digite o nome do produto que deseja remover: ")

if produto in produtos:
    del produtos[produto]
    print(f"Produto '{produto}' removido com sucesso.")
else:
    print(f"Produto '{produto}' não encontrado.")

print("Dicionário final:")
print(produtos)