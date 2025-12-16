class Animal():
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome:str, idade:int, raca:str):
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_som(self):
        print("au au")

class Gato(Animal):
    def __init__(self, nome:str, idade:int, especie:str):
        super().__init__(nome, idade)
        self.especie = especie

    def fazer_som(self):
        print("miau")

cao = Cachorro("Rex", 4, "Vira Lata")
gato = Gato("Felix", 2, "persa")

def emitir_som(animal:Animal):
    animal.fazer_som()

emitir_som(cao)
emitir_som(gato)