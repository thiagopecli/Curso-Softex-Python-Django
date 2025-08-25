# Curso-Softex-Python-Django

print("Bem-vindo à Padaria!")
while True:
    tipo_pao = input("Digite o tipo de pão (francês, doce, forma, australiano) ou 'sair' para encerrar: ")
    if tipo_pao == 'sair':
        break
    quantidade = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor do pão: "))
    forma_pagamento = input("Digite a forma de pagamento (dinheiro, cartão): ")
    forma_entrega = input("Digite a forma de entrega (retirada, entrega): ")
    if forma_entrega == "entrega":
        nome_cliente = input("Digite o nome do cliente: ")
        endereco = input("Digite o endereço de entrega: ")
        bairro = input("Digite o bairro: ")
        valor_frete = 5.0  # Valor fixo para o frete
    nome_atendente = input("Digite o nome do atendente: ")
    codigo_entrega = 12345  # Código fixo para a entrega

    print("Resumo do Pedido:")
    print(f"Tipo de Pão: {tipo_pao}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor: {valor}")
    print(f"Forma de Pagamento: {forma_pagamento}")
    print(f"Forma de Entrega: {forma_entrega}")
    if forma_entrega == "entrega":
        print(f"Nome do Cliente: {nome_cliente}")
        print(f"Endereço: {endereco}")
        print(f"Bairro: {bairro}")
        print(f"Valor do Frete: {valor_frete}")
    print(f"Nome do Atendente: {nome_atendente}")
    print(f"Código da Entrega: {codigo_entrega}")