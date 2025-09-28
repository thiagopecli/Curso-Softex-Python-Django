"""4.  Hierarquia de Classes e Dicionários: Crie uma hierarquia de classes para
um sistema de controle de estoque. Comece com uma classe Produto com atributos
como nome e preco. Em seguida, crie classes filhas como Eletronico e Roupa. A 
classe Estoque deve usar um dicionário para armazenar os produtos, onde a chave
é o nome do produto e o valor é o objeto do produto."""

class Produto():
    def __init__(self, nome:str, preco:float) -> None:
        self.nome = nome
        self.preco = preco

class Eletronico(Produto):
    def __init__(self, nome: str, preco: float) -> None:
        super().__init__(nome, preco)

class Roupa(Produto):
    def __init__(self, nome: str, preco: float) -> None:
        super().__init__(nome, preco)

class Estoque():
    def __init__(self) -> None:
        self.produtos = {}
    def adicionar_produto(self, produto:Produto) -> None:
        self.produtos[produto.nome] = produto
    def listar_produtos(self) -> None:
        for produto in self.produtos.values():
            print(f"Produto: {produto.nome}, Preço: R$ {produto.preco:.2f}")

estoque = Estoque()
laptop = Eletronico(nome="Laptop", preco=3500.00)
camiseta = Roupa(nome="Camiseta", preco=79.90)

estoque.adicionar_produto(laptop)
estoque.adicionar_produto(camiseta)
estoque.listar_produtos()