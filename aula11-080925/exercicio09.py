"""9.  Crie um dicionário com os nomes de 5 alunos e suas notas. Percorra o dicionário e 
imprima apenas os alunos que tiraram nota maior que 7."""

alunos = {
    "Alice": 8,
    "Bob": 6,
    "Charlie": 7.5,
    "David": 9,
    "Eva": 5
}

for nome, nota in alunos.items():
    if nota > 7:
        print(f"Aluno: {nome}, Nota: {nota}")