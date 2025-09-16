"""7.  Conversor de Temperatura: Crie uma função que receba uma temperatura em Celsius 
e a converta para Fahrenheit. A fórmula é: F = (C * 9/5) + 32. Imprima o resultado."""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

resultado = celsius_para_fahrenheit(25)
print(f"A temperatura em Fahrenheit é: {resultado}")