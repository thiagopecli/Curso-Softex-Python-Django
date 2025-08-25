"""
Exercício: Simulação de Pedido em uma Lanchonete

Crie um programa que simula um sistema de pedido em uma lanchonete:
1. Defina o preço do hamburguer;
2. Defina um código de cupom desconto;
3. O programa deve pedir ao cliente o nome do produto repetidamente até que o produto correto seja digitado;
4. Após a eescolha, o programa deve perguntar se o cliente tem um cupom de deconto;
5. Se o cliente digitar o cupom corretamente, aplique o desconto;
6. Calcule o preço final e exiba o total a pagar;
7. O programa deve encerrar após o pedido ser finalizado.  

"""

preco_hamburguer = 27.99
codigo_cupom = "DESCONTO10"
desconto = 0.1
produto = ""

while produto.lower() != "hamburguer":
    produto = input("Digite o nome do produto que deseja (hamburguer): ")
    if produto.lower() != "hamburguer":
        print("Produto inválido. Por favor, tente novamente.")
    else:
        print("Produto selecionado: Hamburguer")
        tem_cupom = input("Você tem um cupom de desconto? (s/n): ")
        if tem_cupom.lower() == 's':
            cupom = input("Digite o código do cupom: ")
            if cupom == codigo_cupom:
                preco_final = preco_hamburguer * (1 - desconto)
                print(f"Cupom válido! Você recebeu um desconto de 10%.")
            else:
                preco_final = preco_hamburguer
                print("Cupom inválido. Nenhum desconto aplicado.")
        else:
            preco_final = preco_hamburguer
            print("Nenhum cupom aplicado.")
        print(f"O total a pagar é: R$ {preco_final:.2f}")
        print("Obrigado pelo seu pedido! Encerrando o programa.")