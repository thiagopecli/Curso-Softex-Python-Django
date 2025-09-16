# Peça para que o usuario digite o preço original do produto (float)
# Se o preço for maior que R$ 100,00, aplique o desconto de 10 % e imprima o valor ajustado
# Use o operador de multiplicação e subtração

preco_produto = float(input("Digite o preço do produto: R$ "))
if preco_produto > 100:
    valor_desconto = preco_produto * 0.10
    preco_ajustado = preco_produto - valor_desconto

    print(preco_ajustado)

#################################################################################

# Calculadora de Desconto:
# Peça ao usuario para digitar o preço do produto(float)
# Aplique desconto de 15% e imprima o valor atualizado

# print("\n--- Calculadora de Desconto ---")

# valor = float(input("\nDigite o valor do produto: R$"))
# porcentagem_desconto = int(input("Digite o desconto: "))

# if valor > 0:
#     desconto_decimal = porcentagem_desconto / 100
#     valor_atualizado = valor * desconto_decimal
#     valor_ajustado = valor - valor_atualizado
#     print(f"Você teve {porcentagem_desconto}% de desconto. ")
#     print(f"Valor com Desconto: R${valor_ajustado:.2f}")

#################################################################################

# print("\n---- Aplicador de Desconto ---")

# while True:
#     print("\nEscolha uma opção: ")
#     print("1. Desconto Cliente")
#     print("2. Desconto Colaborador")
#     print("3. Desconto Defeito")
#     print("4. Sair")

#     escolha = input("Escolha uma opção: ")

#     if escolha == "1":
#         valor1 = float(input("\nDigite o valor do produto: R$ "))
#         desconto_cliente = 0.15
#         valor1_desconto = valor1 * desconto_cliente
#         valor1_ajustado = valor1 - valor1_desconto
#         print(f"\nValor com Desconto: {valor1_ajustado:.2f}")
#         break

#     elif escolha == "2":
#         valor2 = float(input("\nDigite o valor do produto: R$ "))
#         desconto_colaborador = 0.30
#         valor2_desconto = valor2 * desconto_colaborador
#         valor2_ajustado = valor2 - valor2_desconto
#         print(f"\nValor com Desconto: {valor2_ajustado:.2f}")
#         break
    
#     elif escolha == "3":
#         valor3 = float(input("\nDigite o valor do produto: R$ "))
#         desconto_defeito = 0.40
#         valor3_desconto = valor3 * desconto_defeito
#         valor3_ajustado = valor3 - valor3_desconto
#         print(f"\nValor com Desconto: {valor3_ajustado:.2f}")
#         break

#     elif escolha == "4":
#         print("Saindo...")
#         break

#     else:
#         print("Opção inválida.")