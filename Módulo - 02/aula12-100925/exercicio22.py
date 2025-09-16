"""22. Calculadora Segura: Crie uma função dividir(a, b) que retorne o resultado da divisão. 
Use try/except para capturar o erro de divisão por zero e retorne uma mensagem 
amigável nesse caso. Imprima o resultado."""

def dividir(a: float, b: float) -> str:
    try:
        resultado = a / b
        return f"O resultado da divisão é: {resultado}"
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

resultado = dividir(10, 2)
print(resultado)

resultado = dividir(10, 0)
print(resultado)
