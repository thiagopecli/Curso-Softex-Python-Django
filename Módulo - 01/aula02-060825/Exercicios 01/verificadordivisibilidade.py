# Verificador de Divisibilidade

# Peça ao usuario um numero inteiro
# Verifica se o numero é divisivel por 5 (Use o operador %)
# Se for, imprima "O numero é divisivel por 5"

numero = int(input("Digite um numero: "))
if numero % 5 == 0:
    print(f"O {numero} é divisivel por 5.")
else:
    print(f"O {numero} não é divisivel por 5.")