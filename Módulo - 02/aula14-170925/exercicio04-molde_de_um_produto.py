"""Exercício 4: Molde de um Produto
Crie uma nova classe chamada Produto. Todo produto deve ter nome e preço. 
Depois, crie duas instâncias:
1. Um "Caderno" que custa 15.50.
2. Uma "Caneta" que custa 3.00. Imprima o nome e o preço de cada produto."""

class Produto():
    def __init__(self, nome:str, preco:float) -> None:
        self.nome = nome
        self.preco = preco
        
    def produto(self) -> None:
        print(f"Uma {self.nome} que custa R$ {self.preco:.2f}.")

caderno = Produto("Caderno", 10)
caneta = Produto("Caneta", 2.00)

caderno.produto()
caneta.produto()