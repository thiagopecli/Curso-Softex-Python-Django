"""11. Calculadora de IMC: Crie uma função que receba o peso (em kg) e a altura (em metros) 
e retorne o Índice de Massa Corporal (IMC). A fórmula é: IMC = peso / (altura ** 2). Imprima o resultado."""

def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura ** 2)

resultado = calcular_imc(70, 1.75)
print(f"O IMC é: {resultado:.2f}")