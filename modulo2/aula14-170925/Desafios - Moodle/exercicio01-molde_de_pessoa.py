"""Exercício 1: Molde de uma Pessoa - Crie uma classe chamada Pessoa. 
No "registro de nascimento" (__init__), toda pessoa deve ter um nome 
e uma idade."""

class Pessoa:
    def __init__ (self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade

    def dados(self) -> None:
        print(f"Meu nome é {self.nome}, e eu tenho {self.idade} anos.")

ana = Pessoa("Ana", 29)

ana.dados()