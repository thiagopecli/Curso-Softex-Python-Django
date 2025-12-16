# 8. Senha com validação de letras e numeros:
# Peça uma senha e verifique com .isalnum() se ela contem apenas letras e numeros
# Se for valida, mostre "Senha valida", se não "não é valida".

senha = input("Digite uma senha: ")
senha.isalnum()

if senha.isalnum():
    print(f"A senha '{senha}' é valida.")
else: 
    print(f"A senha '{senha}' não é valida.")