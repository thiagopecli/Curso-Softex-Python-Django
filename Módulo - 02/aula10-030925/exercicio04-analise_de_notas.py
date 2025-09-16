notas = [("Ana", 9.5), ("João", 8.0), ("Maria", 10.0), ("Pedro", 7.5), ("Ana", 10.0), ("Carlos", 6.5)]

maior_nota = 0.0

for _, nota in notas:
    if nota > maior_nota:
        maior_nota = nota
print(maior_nota)

aluno_maior_nota = []

for aluno, nota in notas:
    if nota == maior_nota:
        aluno_maior_nota.append(aluno)

aluno_maior_nota = tuple(aluno_maior_nota)
print(aluno_maior_nota)

aluno_nota_baixa = {aluno for aluno, nota in notas if nota < 7.0}
print(aluno_nota_baixa)