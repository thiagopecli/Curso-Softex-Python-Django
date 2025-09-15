"""5.  Crie um dicionário com 3 produtos e suas quantidades em estoque. Peça ao usuário para 
digitar um nome de produto e uma quantidade para adicionar. Atualize o estoque e 
imprima o dicionário."""

produtos = {
    "cadeira": 10,
    "mesa": 5,
    "quadro": 8
}

produto = input("Digite o nome do produto que deseja adicionar: ")
quantidade = int(input("Digite a quantidade que deseja adicionar: "))

if produto in produtos:
    produtos[produto] += quantidade
else:
    produtos[produto] = quantidade

print(produtos)