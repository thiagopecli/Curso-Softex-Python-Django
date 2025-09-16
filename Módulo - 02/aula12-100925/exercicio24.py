"""24. Gerenciador de Tarefas Interativo: Crie um programa com um menu que usa funções 
para adicionar, remover e listar tarefas em uma lista global. Adicione tratamento de erros 
para entradas inválidas do usuário."""

tarefas = []

def adicionar_tarefa(tarefa: str):
    tarefas.append(tarefa)
    print(f"Tarefa adicionada: {tarefa}")

def remover_tarefa(tarefa: str):
    try:
        tarefas.remove(tarefa)
        print(f"Tarefa removida: {tarefa}")
    except ValueError:
        print(f"Tarefa não encontrada: {tarefa}")

def listar_tarefas():
    if tarefas:
        print("Lista de Tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa}")
    else:
        print("Nenhuma tarefa encontrada.")

def menu():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. Listar Tarefas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(tarefa)
        elif opcao == "3":
            listar_tarefas()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()