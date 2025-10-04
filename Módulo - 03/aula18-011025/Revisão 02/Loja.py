"""Etapa 3: A Loja (no arquivo loja.py) 
 
Uma loja contém muitos produtos. Ela é como um grande contêiner que guarda 
tudo. Isso é o conceito de Composição. 
Seu trabalho aqui: 
●  Crie uma classe chamada Loja. 
●  Esta classe deve ter uma lista para guardar todos os objetos Produto. 
●  Use um dicionário para gerenciar o estoque de cada produto, onde a "chave" 
é o nome do produto e o "valor" é a quantidade disponível. 
●  Crie um método adicionar_produto_ao_estoque() que recebe um produto e a 
quantidade, e o adiciona à sua lista e ao seu dicionário de estoque. 
●  Crie um método verificar_estoque_de_produto() que retorna a quantidade em
estoque de um produto específico. """

from Produto import Produto

class Loja:
    def __init__(self) -> None:
        self.estoque = {}
        self.produtos = []

    def adicionar_produto_estoque(self, produto: Produto, quantidade):
        if produto not in self.produtos:
            self.produtos.append(produto)
        
        self.estoque[produto.nome] = quantidade
        print(f"-> Produto '{produto.nome}' adicionado/atualizado com" 
              f"{quantidade} unidades no estoque.")

    def verificar_estoque_de_produto(self, nome_produto: str):
        return self.estoque.get(nome_produto, 0)
