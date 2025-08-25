# Caixa Eletrônico Simplificado
# ● Defina um saldo inicial.
# ● Use um while True para apresentar um menu ao usuário:
# ○
# 1. Sacar
# ○
# 2. Depositar
# ○
# 3. Ver saldo
# ○
# 4. Sair
# ● Use if-elif-else para processar a escolha do usuário.
# ○ Se sacar, verifique se há saldo suficiente.
# ○ Se depositar, adicione o valor ao saldo.
# ○ Se sair, use break.
# ● Valide as entradas do usuário (por exemplo, não permitir saque de valor negativo).

saldo = 0

while True:
    print("\nMenu:")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Ver saldo")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = float(input("Digite o valor a sacar: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor < 0:
            print("Valor inválido.")
        else:
            saldo -= valor
            print("Saque realizado com sucesso.")

    elif escolha == "2":
        valor = float(input("Digite o valor a depositar: "))
        if valor < 0:
            print("Valor inválido.")
        else:
            saldo += valor
            print("Depósito realizado com sucesso.")

    elif escolha == "3":
        print("Saldo atual:", saldo)

    elif escolha == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")