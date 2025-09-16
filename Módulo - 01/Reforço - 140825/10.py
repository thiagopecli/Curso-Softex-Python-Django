"""Crie um programa que simula um login. Ele deve pedir um nome de usuário (admin) e uma 
senha (senha123). O programa deve permitir apenas uma tentativa. """

usuario = "admin"
chave = "senha123"
tentativa = 2

for tentativa_atual in range(tentativa):
    login = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if login == usuario and senha == chave:
        print("Acesso permitido!")
        break
    else: 
        print("Acesso negado!")
        tentativa_restante = tentativa - (tentativa_atual + 1)
        if tentativa_restante > 0:
            print(f"Você tem só mais {tentativa_restante} tentativas.")
else: 
    print("\n Número máximo de tentativas excedido. Acesso bloqueado!")