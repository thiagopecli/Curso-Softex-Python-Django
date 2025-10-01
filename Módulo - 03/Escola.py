from Estudante import Estudante

class Escola():
    def __init__(self) -> None:
        self.estudantes = []
    
    def adicionar_estudante(self, estudante):
        self.estudantes.append(Estudante)
        print(f"Estudante '{estudante.nome}' adicionado a Escola.")

