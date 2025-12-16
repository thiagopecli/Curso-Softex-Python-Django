# 11. Validador de senha forte
# Uma Senha com no minimo 8 caracteres, uma letra maiuscula, uma minuscula, e um numero


# while True:
#     print("Uma Senha com no minimo 8 caracteres, uma letra maiuscula, uma minuscula, e um numero!")
#     senha = input("Digite uma senha: ")

#     if len(senha) < 8:
#         print("Senha muito curta! Deve ter ao menos 8 caracteres.")
#     elif not any(c.islower() for c in senha):
#         print("A senha fraca.")
#     elif not any(c.isupper() for c in senha):
#         print("A senha fraca.")
#     elif not any(c.isdigit() for c in senha):
#         print("A senha fraca.")
#     else:
#         print("Senha forte!")
#         break


###############################################################################

def senha_forte(senha):
    if len(senha) < 8:
        return "Senha muito curta! Deve ter ao menos 8 caracteres."
    if senha.lower() == senha:
        return "A senha deve conter ao menos uma letra maiúscula."
    if senha.upper() == senha:
        return "A senha deve conter ao menos uma letra minúscula."
    if not any(c.isdigit() for c in senha):
        return "A senha deve conter ao menos um número."
    return "ok"

print("Uma Senha com no minimo 8 caracteres, uma letra maiuscula, uma minuscula, e um numero!")

while True:
    senha = input("Digite uma senha: ")
    resultado = senha_forte(senha)
    if resultado == "ok":
        print("Senha forte!")