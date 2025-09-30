"""5. Casa e Cômodos (Médio) 
 
●  Classes: Comodo e Casa. 
●  Classe Comodo: 
○  Atributo: nome. 
○  Método: __init__(nome). 
●  Classe Casa: 
○  Atributo (Composição): comodos, que deve ser uma lista vazia. 
○  Método: __init__ que inicializa a lista comodos. 
○  Método: adicionar_comodo(nome) que cria uma instância de Comodo e a adiciona 
na lista comodos. 
○  Método: listar_comodos() que itera sobre a lista e imprime o nome de cada 
cômodo. """

class Comodo:
    def __init__(self, nome:str):
        self.nome = nome

class Casa:
    def __init__(self) -> None:
        self.comodos = []

    def adicionar_comodos(self, nome_do_comodo:str):
        novo_comodo = Comodo(nome=nome_do_comodo)
        self.comodos.append(novo_comodo)
        print(f"O cômodo '{nome_do_comodo}' foi adicionado à casa. ")
    
    def listar_comodos(self):
        if not self.comodos:
            print("A casa ainda não tem cômodos. ")
        else:
            for comodo in self.comodos:
                print(f"- {comodo.nome}")

minha_casa = Casa()
minha_casa.adicionar_comodos("Sala")
minha_casa.adicionar_comodos("Banheiro")
minha_casa.listar_comodos()