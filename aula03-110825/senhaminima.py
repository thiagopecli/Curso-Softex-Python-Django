# Senha minima
# Solicite uma senha e verifique se a ela tem pelo menos 8 caracteres usando len()

senha = (input("Digite uma senha com no mínimo 8 caracteres: "))

if len(senha) >= 8:
    print("Senha válida")
else:
    print("Senha inválida")
