"""Nível Avançado: Interação e Organização 
Estes exercícios envolvem como as classes e objetos podem interagir entre si e 
conceitos um pouco mais complexos. 

Exercício 9: Atributo da Classe (Funcionários da Empresa) 
Crie uma classe Funcionario. Cada funcionário terá nome e salário (atributos 
de instância). 
Agora, crie um atributo de classe chamado percentual_bonus, com o valor 1.10 
(representando 10% de bônus). 
Crie um método aplicar_bonus que multiplica o salário do funcionário pelo 
percentual_bonus da classe. Crie dois funcionários com salários diferentes, 
aplique o bônus e veja o resultado. 
●  Dica: Um atributo de classe é definido diretamente dentro da classe, fora 
de qualquer método."""

class Funcionario():
    percentual_bonus = 1.10
    
    def __init__(self, nome:str, salario:float) -> None:
        self.nome = nome
        self.salario = salario
    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
    def mostrar_dados(self):
        print(f"Funcionário: {self.nome}, Salário: R$ {self.salario:.2f}.")

func_ana = Funcionario("Ana", 5000.00)
func_joao = Funcionario("João", 8000.00)

func_ana.mostrar_dados()
func_joao.mostrar_dados()

func_ana.aplicar_bonus()
func_joao.aplicar_bonus()

func_ana.mostrar_dados()
func_joao.mostrar_dados()