"""Escreva um programa que solicita a senha do usuário. A senha deve ter no mínimo 6 
caracteres. Se não tiver, imprima uma mensagem de erro."""

while True:
    senha = input("Digite uma senha com no mínimo 6 caracteres: ")
    if len(senha) >= 6:
        print("Senha criada com sucesso!")
        break
    else:
        print("Digite novamente!")
        continue