"""8.  Herança Múltipla com Dicionários e Conjuntos: (Este é um desafio um 
pouco mais avançado) Crie uma classe Funcionario com atributos como nome e um
método trabalhar(). Crie uma classe Gerente que herda de Funcionario e adicione
um atributo privado __equipe que é um conjunto. Use um método add_membro() para
adicionar membros."""

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):
        return f"{self.nome} está trabalhando."

class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
        self.__equipe = set()

    def add_membro(self, funcionario):
        self.__equipe.add(funcionario)
        return f"{funcionario.nome} foi adicionado à equipe de {self.nome}."
    def mostrar_equipe(self):
        return [funcionario.nome for funcionario in self.__equipe]

if __name__ == "__main__":  
    gerente = Gerente("Alice")
    func1 = Funcionario("Bob")
    func2 = Funcionario("Charlie")

    print(gerente.trabalhar())
    print(gerente.add_membro(func1))
    print(gerente.add_membro(func2))
    print("Equipe do gerente:", gerente.mostrar_equipe())