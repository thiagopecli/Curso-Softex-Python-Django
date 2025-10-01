from Pessoa import Pessoa

materias = {}

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula:int) -> None:
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = {}

    def adicionar_notas(self, materia:str, nota: float):
        
        if materia in self.notas:
            self.notas[materia].append(nota)
        else:
            materias[materia] = [nota]
        print(f"A nota '{nota}' foi adicionado a materia '{materias}'.")

carlos = Estudante(nome="Carlos", idade=25, matricula=15234)
carlos.adicionar_notas("matematica", 8.0)
carlos.adicionar_notas("portugues", 8.0)
carlos.adicionar_notas("matematica", 7.5)

print(materias)