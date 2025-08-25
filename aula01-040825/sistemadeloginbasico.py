# Defina um nome de usuario e uma senha:
usuario = "thiago"
senha = 1234
# Use um loop while true para pedir ao usuario que digite o nome e senha:
while True:
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite sua senha: ")
# Se ambos estiverem corretor, imprima "Login bem sucedido" e use break para sair do loop.
    if usuario == "thiago" and senha == "1234":
        print("Login bem sucedido!")
        break
    else:
        print("Login invalido, tente novamente!")
