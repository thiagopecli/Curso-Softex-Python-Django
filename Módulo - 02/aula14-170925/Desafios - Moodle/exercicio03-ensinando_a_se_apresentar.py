"""Exercício 3: Ensinando a se Apresentar
Adicione um método (uma "ação") à sua classe Pessoa chamado apresentar. 
Esse método deve imprimir uma frase como: "Olá, meu nome é [nome] e eu tenho 
[idade] anos." Chame esse método para os objetos "João" e "Maria"."""

class Pessoa():
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade

    def dados(self) -> None:
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos.")
joao = Pessoa("João", 25)
ana = Pessoa("Ana", 30)

joao.dados()
ana.dados()