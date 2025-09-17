class Cachorro:
    def __init__(self, nome:str, cor:str)-> None:
        self.nome = nome
        self.cor = cor

    def latir(self, fala:str) -> None:
        print(f"{self.nome} diz: {fala}au au!")

rex = Cachorro("rex", "preto")
bela = Cachorro("bela", "branco")

print(f"Meu cachorro se chama {rex.nome} e tem a cor {rex.cor}")
rex.latir("")