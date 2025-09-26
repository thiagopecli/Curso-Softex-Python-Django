"""Encapsulamento e Dicionários: Crie uma classe Pessoa com os atributos privados 
__nome e __idade. Use um método get_info() que retorne os dados da pessoa como um 
dicionário no formato {'nome': '...', 'idade': '...'}."""

class Pessoa():
    def __init__(self, __nome, __idade) -> None:
        self.__nome = __nome
        self.__idade = __idade
    def get_info(self) -> dict:
        return {'nome': self.__nome, 'idade': self.__idade}

pessoa1 = Pessoa("Ana", 28)
info = pessoa1.get_info()
print(info)

""" 

class Pessoa():
    def __init__(self, __nome:str, __idade:int) -> None:
        self.__nome = __nome
        self.__idade = __idade
    def get__info(self) -> dict:
        return {'nome': self.__nome, 'idade':self.__idade}

pessoa1 = Pessoa("Ana", 28)
info = pessoa1.get_info()
print(info)

class Pessoa():
    def __init__(self, __nome, __idade) -> None:
        self.__nome = __nome
        self.__idade = __idade
    def get_info(self) -> dict:
        return {'nome': self.__nome, 'idade': self.__idade}
    
pessoa01 = Pessoa("Ana", 30)
info = pessoa01.get_info()
print(info)

"""