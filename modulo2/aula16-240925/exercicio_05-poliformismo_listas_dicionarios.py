"""5.  Polimorfismo e Listas de Dicionários: Usando as classes do exercício 4, crie uma lista 
de dicionários, onde cada dicionário representa um produto e suas informações. Crie 
uma classe CarrinhoDeCompras que receba essa lista e use polimorfismo para calcular o 
total da compra. """

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

class CarrinhoDeCompras():
    def __init__(self, produtos:list[Produto]) -> None:
        self.produtos = produtos
    def calcular_total(self) -> float:
        total = sum(produto.preco for produto in self.produtos)
        return total
    
laptop = Eletronico(nome="Laptop", preco=3500.00)
camiseta = Roupa(nome="Camiseta", preco=79.90)

carrinho = CarrinhoDeCompras(produtos=[laptop, camiseta])
total_compra = carrinho.calcular_total()

print(f"Total da Compra: R$ {total_compra:.2f}")
