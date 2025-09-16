# 1. Comparando nomes ignorando maiusculas
# Peça dois nomes e verifique se são iguais usando .lower()
# Se forem iguais, mostre "Nomes Iguais", senão "Nomes Diferentes".

nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

if nome1.lower() == nome2.lower():
    print("Os dois nomes são iguais! ")
else:
    print("Os dois nomes são diferentes! ")