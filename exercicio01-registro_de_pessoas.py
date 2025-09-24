"""1. Nível Fácil: Registro de Pessoas 
 
Crie uma classe base Pessoa com um construtor que recebe nome e idade. Adicione um 
método apresentar() que imprime uma frase com o nome e a idade da pessoa. 

Em seguida, crie uma classe Estudante que herda de Pessoa. O construtor de Estudante deve 
chamar o construtor da classe pai e adicionar um atributo para o curso. A classe Estudante 
deve sobrescrever o método apresentar() para incluir o curso na frase. 
Por fim, crie uma lista com um objeto Pessoa e um objeto Estudante. Itere sobre a lista e 
chame o método apresentar() para cada item, demonstrando o polimorfismo. """

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos. ")

class Estudante(Pessoa):
    def __init__(self, nome:str, idade:int, curso:str):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e faço {self.curso}. ")

paulo = Pessoa("Paulo", 25)
carlos = Estudante("Carlos", 30, "Historia")
lista = [paulo, carlos]

for obejeto in lista:
    obejeto.apresentar()