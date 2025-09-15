"""Nível 2: Manipulação e Iteração (Exercícios 6-10) 
 
6.  Crie um dicionário com 4 nomes e idades. Percorra o dicionário e imprima cada nome e 
idade no formato "Nome: [Nome], Idade: [Idade]"."""

pessoas = {
    "Ana": 28,
    "Bruno": 34,
    "Carla": 22,
    "Daniel": 45
}

for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")