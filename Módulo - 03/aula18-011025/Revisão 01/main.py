"""Etapa 4: Juntando Tudo (no arquivo main.py) 
 
Este é o arquivo principal, onde você vai "ligar o motor" e ver tudo 
funcionando. 
Seu trabalho aqui: 
●  Importe as classes Escola e Estudante que você criou. 
●  Crie uma instância (um objeto) da sua Escola. 
●  Crie pelo menos dois objetos da sua classe Estudante, dando a cada um um 
nome, idade e matrícula. 
●  Use os métodos que você criou para: 
○  Adicionar algumas matérias e notas para cada estudante. 
○  Adicionar os estudantes à sua Escola. 
●  Chame o método mostrar_relatorio() da sua Escola para ver a mágica 
acontecer!"""

from Escola import Escola
from Estudante import Estudante

minhas_escola = Escola()
print("Criando Alunos")

aluno1 = Estudante(nome="Carlos", idade=30, matricula=202545)
aluno2 = Estudante(nome="Amanda", idade=19, matricula=252545)
print(f"Aluno '{aluno1.get_nome()}' criado. ")
print(f"Aluno '{aluno2.get_nome()}' criado. ")

print("Adicionando Notas")
aluno1.adicionar_notas("Geografia", 7.2)
aluno1.adicionar_notas("Geografia", 5)
aluno1.adicionar_notas("Inglês", 9.2)

aluno2.adicionar_notas("Historia", 9.2)
aluno2.adicionar_notas("Geografia", 7)
aluno2.adicionar_notas("Artes", 9.2)

print("Matriculando os Alunos")
minhas_escola.adicionar_estudante(aluno1)
minhas_escola.adicionar_estudante(aluno2)

minhas_escola.mostrar_relatorio()