"""6.  Encapsulamento e Conjuntos: Crie uma classe RedeSocial com um atributo
privado __amigos, que deve ser um conjunto para garantir que não haja 
duplicatas. Implemente os métodos adicionar_amigo() e remover_amigo(). """

class RedeSocial():
    def __init__(self) -> None:
        self.__amigos = set()
    
    def adicionar_amigo(self, nome:str) -> None:
        self.__amigos.add(nome)
    
    def remover_amigo(self, nome:str) -> None:
        self.__amigos.discard(nome)
    
    def listar_amigos(self) -> None:
        for amigo in self.__amigos:
            print(f"Amigo: {amigo}")

rede_social = RedeSocial()
rede_social.adicionar_amigo("Alice")
rede_social.adicionar_amigo("Bob")
rede_social.adicionar_amigo("Alice")  # Tentativa de adicionar duplicata
rede_social.listar_amigos()
rede_social.remover_amigo("Bob")
print("Após remover Bob:")
rede_social.listar_amigos()
