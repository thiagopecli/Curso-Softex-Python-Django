"""22. Sistema de Pontuação: Crie um dicionário de jogadores e suas pontuações iniciais. 
Simule uma rodada de jogo, atualizando a pontuação de um jogador específico. Permita 
que o usuário adicione novos jogadores e pontue-os."""

jogadores = {}

def adicionar_jogador(nome):
    if nome not in jogadores:
        jogadores[nome] = 0
        print(f"Jogador {nome} adicionado com sucesso!")
    else:
        print(f"Jogador {nome} já existe.")

def atualizar_pontuacao(nome, pontos):
    if nome in jogadores:
        jogadores[nome] += pontos
        print(f"Pontuação de {nome} atualizada para {jogadores[nome]}.")
    else:
        print(f"Jogador {nome} não encontrado.")

while True:
    print("--- Sistema de Pontuação ---")
    print("\n1- Adicionar Jogador", "\n2- Atualizar Pontuação", "\n3- Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do jogador: ").lower()
        adicionar_jogador(nome)

    elif opcao == "2":
        nome = input("Digite o nome do jogador: ").lower()
        pontos = int(input("Digite a quantidade de pontos a adicionar: "))
        atualizar_pontuacao(nome, pontos)

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 3.")
    print()