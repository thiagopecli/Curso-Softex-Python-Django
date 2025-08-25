# Defina uma senha secreta em uma variavell (str)
# Peça para o usuario digitar a senha
# Use if e else para verificar a senha

senha = "thiago123"
senha2 = input("Digite a senha: ")

confirmacao = senha == senha2
if confirmacao:
    print("Senha confirmada.")
else:
    print("Senha incorreta.")

#################################################################################

# print("\n---Verificador de Senhas ---")
# tentativa = 0

# while tentativa < 3:
#     senha1 = (input("\nDigite a senha: "))
#     senha2 = (input("\nDigite confirme a senha: "))

#     confirmacao = senha1 == senha2
#     if confirmacao:
#         print("Senha confirmada, acesso liberado. ")
#         break
#     else:
#         print("Senha incorreta, acesso negado. ")
#         tentativa += 1

#     if tentativa >= 3:
#         print("Conta Bloqueada!")

#################################################################################