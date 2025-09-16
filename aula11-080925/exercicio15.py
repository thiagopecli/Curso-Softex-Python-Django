"""15. Crie um dicionário com os nomes de 3 pessoas e seus hobbies (em formato de conjunto). 
Peça ao usuário para digitar o nome de uma pessoa e imprima seus hobbies"""

pessoas_hobbies = {
    "alice": {"leitura", "natação", "jardinagem"},
    "bob": {"futebol", "videogames", "cinema"},
    "carlos": {"pintura", "caminhadas", "fotografia"}
}

nome = input("Digite o nome de uma pessoa: ").lower()

if nome in pessoas_hobbies:
    print(f"Hobbies de {nome}: {', '.join(pessoas_hobbies[nome])}")
else:
    print("Pessoa não encontrada.")