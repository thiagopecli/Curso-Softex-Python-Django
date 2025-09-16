# 7. Verificando numero
# Peça ao usuario algo e use .isdigit() para verificar se é um numero valido

numero = input("digite um numero: ")
numero.isdigit()

if numero.isdigit():
    print(f"O número {numero} é um digito válido. ")
else:
    print(f"'{numero}' não é valido.")