class Animal():
    def __init__(self, nome:str) -> None:
        self.nome = nome
    def fazer_som(self) -> str:
        return "som de animal generico"
    def apresentar(self):
        pass
    def __str__(self) -> str:
        return f"{type(self).__name__}({self.nome})"
class Gato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    def fazer_som(self) -> str:
        return "Miau"
    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu faço '{self.fazer_som()}'!")
class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
    def fazer_som(self) -> str:
        return "Au au"
    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu faço '{self.fazer_som()}'!")

gato = Gato("Felix")
cachorro = Cachorro("Ronaldo")

lista = (gato, cachorro)

def emitir_som(animal:Animal):
    print(animal.fazer_som())

# emitir_som(gato)
# emitir_som(cachorro)

def apresentacao(apresentadando:Animal):
    apresentadando.apresentar()

apresentacao(gato)
apresentacao(cachorro)