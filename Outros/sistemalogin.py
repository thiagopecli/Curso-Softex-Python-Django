# Sistema de login basico:
tentativas = 0
login = "admin"
senha = 1234
while tentativas < 3:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha:")
    if login == "admin":
        break
    if senha == "1234":
        print("Acesso Permitido!")
        break
    else:
        print("Login incorreto, tente novamente!")
        tentativas += 1