"""10. Projeto de Sistema de Pedidos: Crie um sistema de pedidos de restaurante. 
○  Crie uma classe ItemMenu com atributos como nome e preco. 
○  Crie classes filhas, Bebida e Prato, que herdam de ItemMenu e podem ter 
atributos adicionais (como tamanho para a Bebida). 
○  Crie uma classe Pedido que use um dicionário para armazenar os itens e suas 
quantidades, e tenha um método polimórfico calcular_total() que itera sobre os
itens do pedido para somar o valor final. """

class ItemMenu:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def detalhes(self):
        return f"{self.nome}: R${self.preco:.2f}"

class Bebida(ItemMenu):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def detalhes(self):
        return f"{self.nome} ({self.tamanho}): R${self.preco:.2f}"

class Prato(ItemMenu):
    def __init__(self, nome, preco, tipo):
        super().__init__(nome, preco)
        self.tipo = tipo

    def detalhes(self):
        return f"{self.nome} ({self.tipo}): R${self.preco:.2f}"

class Pedido:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item, quantidade):
        if item not in self.itens:
            self.itens[item] = 0
        self.itens[item] += quantidade

    def calcular_total(self):
        total = sum(item.preco * quantidade for item, quantidade in self.itens.items())
        return f"Total do pedido: R${total:.2f}"
    def detalhes_pedido(self):
        detalhes = [f"{item.detalhes()} x {quantidade}" for item, quantidade in self.itens.items()]
        return "\n".join(detalhes)
    
if __name__ == "__main__":
    bebida1 = Bebida("Coca-Cola", 5.00, "500ml")
    prato1 = Prato("Hambúrguer", 15.00, "Carne")

    pedido = Pedido()
    pedido.adicionar_item(bebida1, 2)
    pedido.adicionar_item(prato1, 1)

    print("Detalhes do Pedido:")
    print(pedido.detalhes_pedido())
    print(pedido.calcular_total())