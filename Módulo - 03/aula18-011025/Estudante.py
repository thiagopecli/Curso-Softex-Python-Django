"""Etapa 2: O Estudante Especializado (no arquivo estudante.py) 
 
Um estudante é uma pessoa, mas tem algumas características extras. Ele tem uma
matrícula e tira notas. 
Seu trabalho aqui: 
●  Crie uma classe chamada Estudante que herda (pega emprestado) todas as 
características da classe Pessoa. 
●  Adicione um atributo de matrícula a esta classe. 
●  Para guardar as notas, use um dicionário, onde a "chave" é o nome da matéria
(como 'Matemática') e o "valor" é uma lista de notas (ex: [9.0, 8.5]). 
●  Crie um método "setter" para adicionar notas a uma matéria específica. Um
"setter" é uma forma de definir ou alterar uma informação dentro do objeto. """

from Pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome: str, idade: int, matricula:int) -> None:
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = {}

    def adicionar_notas(self, materia:str, nota: float):
        
        if materia in self.notas:
            self.notas[materia].append(nota)
        else:
            self.notas[materia] = [nota]
        print(f"Nota {nota} adicionada para a matéria '{materia}' de "
              f"{self.get_nome()}.")

carlos = Estudante(nome="José", idade=25, matricula=15234)

carlos.adicionar_notas("matematica", 8.0)
carlos.adicionar_notas("portugues", 9.0)
carlos.adicionar_notas("matematica", 7.5)

print(f"Nome do estudante: {carlos.get_nome()}.")
print(f"Matricula do {carlos.get_nome()}: {carlos.matricula}.")
print(f"Notas do {carlos.get_nome()}: {carlos.notas}.")