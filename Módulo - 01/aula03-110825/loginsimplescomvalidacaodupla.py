# Login simples com validação dupla

# Peça ao usuario para digitar o usuario e senha
# o login só é aceito se o usuario contiver "admin" (in) e a senha tiver no minimo 6 caracteres (len())

usuario = input("Digite seu usuário: ")
senha = input("Digite a senha: ")

if "admin" in usuario and len(senha) >= 6:
    print("Login aceito.")
else:
    print("Login inválido.")