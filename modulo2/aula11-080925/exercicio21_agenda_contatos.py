import re

"""Nível 5: Casos de Uso e Aplicações Complexas (Exercícios 21-25) 
 
21. Agenda de Contatos: Crie um sistema simples de agenda que use um dicionário. Use 
um loop while para mostrar um menu com opções de "adicionar contato", "buscar 
contato" e "sair". Use if para lidar com as opções do menu."""

agenda = {}

def telefone_valido(telefone):
    """Aceita formatos como: 99999-9999, (99)99999-9999, 999999999, etc."""
    padrao = r'^(\(?\d{2}\)?\s?)?\d{4,5}-?\d{4}$'
    return re.match(padrao, telefone) is not None

while True:
    print("--- Agenda ---")
    print("\n1- Adicionar contato", "\n2- Buscar Contato", "\n3- Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ").lower()
        telefone = input("Digite o telefone do contato: ")
        if telefone_valido(telefone):
            agenda[nome] = telefone
            print("Contato adicionado com sucesso!")
        else:
            print("Telefone inválido! Use um formato válido, ex: 99999-9999 ou (99)99999-9999.")

    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja buscar: ").lower()
        telefone = agenda.get(nome, "Contato não encontrado.")
        print(f"Telefone de {nome}: {telefone}")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 3.")
    print()