"""Etapa 3: A Escola (no arquivo escola.py) 
 
Uma escola é um lugar que contém muitos estudantes. Ela não é um estudante, mas
tem uma coleção deles. Isso é o conceito de Composição. 
Seu trabalho aqui: 
●  Crie uma classe chamada Escola. 
●  Esta classe deve ter uma lista para guardar todos os objetos Estudante. 
●  Crie um método adicionar_estudante() para colocar novos estudantes na lista
da escola.
●  Crie um método mostrar_relatorio() que percorre a lista de estudantes e 
imprime todas as suas informações: nome, matrícula, e as notas de cada 
matéria."""

from Estudante import Estudante

class Escola():
    def __init__(self) -> None:
        self.estudantes = []
    
    def adicionar_estudante(self, estudante: Estudante):
        self.estudantes.append(estudante)
        print(f"Estudante '{estudante.get_nome()}' adicionado a Escola.")

    def mostrar_relatorio(self):
        print(f"Relatório de Alunos da Escola:")

        if not self.estudantes:
            print("A escola não tem estudantes matriculados.")
        else:
            for aluno in self.estudantes:
                print(f"Nome: {aluno.get_nome()}.")
                print(f"Matricula: {aluno.matricula}.")
                print(f"Notas: {aluno.notas}.")

minha_escola = Escola()

aluno1 = Estudante("Fabricio", 25, 25478)
aluno2 = Estudante("Leandro", 24, 19478)

aluno1.adicionar_notas("matemática", 8)
aluno1.adicionar_notas("historia", 5)
aluno1.adicionar_notas("matemática", 7)

aluno2.adicionar_notas("matemática", 5)
aluno2.adicionar_notas("historia", 7)
aluno2.adicionar_notas("matemática", 9)

print(f"Matriculando os alunos:")
minha_escola.adicionar_estudante(aluno1)
minha_escola.adicionar_estudante(aluno2)

minha_escola.mostrar_relatorio()