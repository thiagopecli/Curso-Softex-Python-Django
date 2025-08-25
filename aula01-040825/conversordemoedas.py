# Conversor de moedas Simples:

valor = float(input("Digite o valor em reais: "))
def converter_para_dolar(valor):
    taxa_de_cambio = 5.00  # Exemplo de taxa de câmbio
    return valor / taxa_de_cambio

valor_em_dolares = converter_para_dolar(valor)
print("Valor em dólares: $", valor_em_dolares)
