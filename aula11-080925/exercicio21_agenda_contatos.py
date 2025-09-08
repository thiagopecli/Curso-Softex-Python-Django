agenda = {}

while True:
    print("--- Agenda ---")
    print("\n1- Adicionar contato", "\n2- Buscar Contato", "\n3- Sair")
    
    if opçao == "1":
        print("Adicionar contato")





    try:
        opçao = input("Digite uma opção: ")
        opçao = int(opçao)

    except ValueError:
        print("Digite um número de 1 a 3!")
        