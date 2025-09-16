"""4.  Verificador de Número Par: Crie uma função que receba um número e retorne True se 
ele for par e False se for ímpar. Imprima o resultado."""

def verificar_par(numero):
    return numero % 2 == 0

resultado = verificar_par(10)
print(f"O número é par? {resultado}")
resultado = verificar_par(7)
print(f"O número é par? {resultado}")