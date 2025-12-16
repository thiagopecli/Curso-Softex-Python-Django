# Conversor de moedas Simples:

valor = float(input("Digite o valor em reais: "))
def converter_para_dolar(valor):
    taxa_de_cambio = 5.00  # Exemplo de taxa de câmbio
    return valor / taxa_de_cambio

valor_em_dolares = converter_para_dolar(valor)
print("Valor em dólares: $", valor_em_dolares)

# Par ou Ímpar(Operadores e if-else):
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Maior de idade (Aninhado de if):
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print(f"{nome}, você é maior de idade!")
else:
    print(f"{nome}, você é menor de idade!")