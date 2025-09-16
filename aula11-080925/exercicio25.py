"""25. Gerenciamento de Tarefas: Crie um dicionário para gerenciar tarefas. As chaves são os 
nomes das tarefas, e os valores são listas de status (ex: ["pendente", "em andamento", 
"concluído"]). Peça ao usuário para adicionar uma tarefa e seu status. Depois, imprima 
apenas as tarefas com status "pendente". """

tarefas = {}

def adicionar_tarefa(nome, status):
    tarefas[nome] = status

def listar_tarefas_pendentes():
    pendentes = [nome for nome, status in tarefas.items() if status == "pendente"]
    if pendentes:
        print("Tarefas pendentes:")
        for tarefa in pendentes:
            print(f"- {tarefa}")
    else:
        print("Não há tarefas pendentes.")

while True:
    print("--- Gerenciamento de Tarefas ---")
    print("\n1- Adicionar Tarefa", "\n2- Listar Tarefas Pendentes", "\n3- Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        status = input("Digite o status da tarefa (pendente, em andamento, concluído): ").lower()
        adicionar_tarefa(nome, status)

    elif opcao == "2":
        listar_tarefas_pendentes()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 3.")
    print()