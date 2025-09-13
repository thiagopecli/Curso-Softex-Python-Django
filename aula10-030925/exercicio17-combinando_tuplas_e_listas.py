"""17. Combinando Tuplas e Listas (Mutabilidade): Crie uma tupla notas_alunos = ('João', 
[7.5, 8.0]). Adicione uma nova nota, 9.5, à lista de notas do aluno."""

notas_alunos = ('João', [7.5, 8.0])
print(f"Tuplas Original: {notas_alunos}")

notas_alunos[1].append(9.5)
print(f"Mesma tupla após adicionar nota: {notas_alunos}")