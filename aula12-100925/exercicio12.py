"""12. Classificador de IMC: Baseado no exercício anterior, crie uma função que receba o IMC 
e retorne a classificação: "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade". 
Use múltiplos if/elif/else. Imprima o resultado."""

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

resultado = classificar_imc(22.5)
print(f"A classificação do IMC é: {resultado}")