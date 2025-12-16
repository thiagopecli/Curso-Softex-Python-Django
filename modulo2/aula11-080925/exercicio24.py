"""24. Sistema de Inventário: Crie um dicionário de inventário de um jogo (ex: "espada": 
{"dano": 50, "peso": 2.5}). Permita que o usuário insira um item no inventário com suas 
características e liste todos os itens. """

inventario = {}

def adicionar_item(nome, dano, peso):
    inventario[nome] = {"dano": dano, "peso": peso}
    print(f"Item '{nome}' adicionado ao inventário.")

def listar_itens():
    if not inventario:
        print("O inventário está vazio.")
    for nome, atributos in inventario.items():
        print(f"Item: {nome}, Dano: {atributos['dano']}, Peso: {atributos['peso']}")

while True:
    print("--- Sistema de Inventário ---")
    print("\n1- Adicionar Item", "\n2- Listar Itens", "\n3- Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do item: ")
        dano = int(input("Digite o dano do item: "))
        peso = float(input("Digite o peso do item: "))
        adicionar_item(nome, dano, peso)

    elif opcao == "2":
        listar_itens()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 3.")
    print()