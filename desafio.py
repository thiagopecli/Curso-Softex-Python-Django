"""
Comércio Padaria: 

1. O programa tem que rodar em loop infinito até ser parado;
2. O cliente fazer o tipo de pão(francês, doce, forma, australiano);
3. Cada pão terá uma quantidade;
4. O valor do pão;
5. Forma de pagamento;
6. Forma de entrega;
7. Dados do cliente(caso seja entrega);
8. Valor do frete por bairro;
9. Nome do Atendente;
10. Código da entrega.

"""

# Tipos de pães
pao_frances = "frances"
pao_doce = "doce"
pao_forma = "forma"

# Valores
valor_pao_frances = 0.50
valor_pao_doce = 5.00
valor_pao_forma = 5.99

# Quantidades
quantidade_pao_frances = 15
quantidade_pao_doce = 20
quantidade_pao_forma = 18

# Nome da atendente
nome_atendente = "Maria"

# Bairros
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

# Frete
frete_barroco = 5.00
frete_sao_jose = 15.00

# Codigo Venda
codigo_venda = 12345

while True:
    print(f"-- Bem-Vindo a padaria, Desespero, sou a atendente {nome_atendente}.")
    escolha = input(f"Temos os pães: {pao_frances}, {pao_doce}, {pao_forma}. Qual pão você deseja? ").lower()
    if escolha == pao_frances:
        quantidade = int(input("Qual a quantidade? "))
        if quantidade < quantidade_pao_frances:
            quantidade_pao_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_pao_frances
            print(f"Seu pedido ficou em R$ {valor_compra}.")
        else:
            print(f"Temos apenas {quantidade_pao_frances} pães {pao_frances} em estoque.")
            break

    forma_retirada = input("É para 1: retirar ou 2: entregar?").lower()
    if forma_retirada == "2":
        bairro_entrega = input(f"Qual o bairro? (1: {bairro_barroco}, 2: {bairro_sao_jose})")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R$ {valor_frete}.")
        elif bairro_entrega == "2":
            valor_frete = frete_sao_jose
            print(f"Valor do frete R$ {valor_frete}.")
        else:
            print("Fora da área de entrega.")
            break
    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Informe seu nome: ")
    forma_pagamento = input("Informe a forma de pagamento (1: Dinheiro, 2: Cartão):")
    if forma_pagamento == "1":
        forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"

    codigo_entrega = codigo_venda + 1

    print(f"O valor total da sua compra é R$ {valor_compra + valor_frete} com o código de entrega {codigo_entrega}.")
    break