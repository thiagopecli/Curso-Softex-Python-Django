# Validação de E-mail 
# ● Use um while True para pedir um e-mail ao usuário. 
# ● Verifique se o e-mail contém o caractere @. 
# ● Se contiver, imprima "E-mail válido" e use break. 
# ● Se não contiver, imprima "E-mail inválido. Digite novamente." 

print("=== Validação de E-mail ===")
while True:
    email = input("Digite seu e-mail: ")
    if "@" in email:
        print("E-mail válido!")
        break
    else:
        print("E-mail inválido. Digite novamente.")
        