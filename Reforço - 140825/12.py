"""Faça um programa que simula a entrada de um sistema. O programa deve pedir uma senha e 
continuar pedindo até que a senha correta ("python123") seja digitada. Use um loop while e 
break. """

# Dados:
chave = "python123"

# Programa de entrada de dados:

# for i in chave:


while True:
    senha = input("Digite a senha: ")

    if senha == chave:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Digite novamente!")
        continue