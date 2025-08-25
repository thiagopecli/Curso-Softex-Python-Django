preco_hamburguer = 37.99
codigo_cupom = "APP10"
desconto = 0.15

while True:
    produto = input("Digite o nome do produto: ")
    if produto.lower() != "hamburguer":
        print("Produto inválido! Digite novamente.")
        continue
    print("Produto selecionado: Hamburguer")
    tem_cupom = input("Você tem cupom de desconto? (s/n): ")
    if tem_cupom.lower() == 's':
        while True:
            codigo = input("Digite o código do desconto: ")
            if codigo == codigo_cupom:
                preco_final = preco_hamburguer * (1 - desconto)
                print("Cupom válido! Você recebeu um desconto de 15%.")
                break
            else:
                print("Cupom inválido!")
                opcao = input("Deseja tentar novamente (t), continuar sem desconto (c) ou sair (s)? ").lower()
                if opcao == 't':
                    continue
                elif opcao == 'c':
                    preco_final = preco_hamburguer
                    print("Nenhum cupom aplicado.")
                    break
                elif opcao == 's':
                    print("Operação cancelada pelo usuário.")
                    exit()
                else:
                    print("Opção inválida. Continuando sem desconto.")
                    preco_final = preco_hamburguer
                    break
    else:
        preco_final = preco_hamburguer
        print("Nenhum cupom aplicado.")
    print(f"O total a pagar é: R$ {preco_final:.2f}.")
    print("Obrigado pelo pedido! Encerrando o programa...")
    break