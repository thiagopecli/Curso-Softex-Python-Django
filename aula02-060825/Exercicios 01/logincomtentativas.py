# Login com Tentativas 
# ● Defina uma senha secreta. 
# ● Use um while True e um contador de tentativas (máximo de 3). 
# ● Se o usuário acertar a senha, imprima "Login bem-sucedido!" e use break. 
# ● Se o usuário errar 3 vezes, imprima "Tentativas esgotadas!" e pare o programa. 

senha_secreta = "7338"
tentativas = 0

print("=== Sistema de Login ===")
print("Você tem 3 tentativas para acertar a senha.")    
while True:
    senha = input("Digite a senha: ")
    tentativas += 1
    
    if senha == senha_secreta:
        print("Login bem-sucedido!")
        break
    elif tentativas >= 3:
        print("Tentativas esgotadas!")
        break
    else:
        print("Senha incorreta. Tente novamente.")  
    