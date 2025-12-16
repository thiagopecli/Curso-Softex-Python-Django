"""9.  Encapsulamento com Listas e Dicionários: Crie uma classe SistemaDeNotas
com um atributo privado __alunos, que é um dicionário onde a chave é o nome do
aluno e o valor é uma lista de suas notas. Implemente os métodos 
adicionar_nota(aluno, nota) e calcular_media(aluno)."""

class SistemaDeNotas:
    def __init__(self):
        self.__alunos = {}

    def adicionar_nota(self, aluno, nota):
        if aluno not in self.__alunos:
            self.__alunos[aluno] = []
        self.__alunos[aluno].append(nota)
        return f"Nota {nota} adicionada para o aluno {aluno}."

    def calcular_media(self, aluno):
        if aluno not in self.__alunos or not self.__alunos[aluno]:
            return f"O aluno {aluno} não tem notas registradas."
        media = sum(self.__alunos[aluno]) / len(self.__alunos[aluno])
        return f"A média do aluno {aluno} é {media:.2f}."

if __name__ == "__main__":
    sistema = SistemaDeNotas()
    print(sistema.adicionar_nota("João", 8.5))
    print(sistema.adicionar_nota("João", 7.0))
    print(sistema.adicionar_nota("Maria", 9.0))
    print(sistema.calcular_media("João"))
    print(sistema.calcular_media("Maria"))
    print(sistema.calcular_media("Pedro"))