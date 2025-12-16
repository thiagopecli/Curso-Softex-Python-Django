"""Nível Avançado (Foco em *args, **kwargs e lambda) 
15. Soma de Números Variáveis: Crie uma função que use *args para somar uma 
quantidade qualquer de números. Imprima o resultado."""

def somar_numeros(*args) -> float:
    return sum(args)

resultado = somar_numeros(1, 2, 3, 4, 5)
print(f"A soma dos números é: {resultado}")