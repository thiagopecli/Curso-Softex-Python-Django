"""20. Retorno de Múltiplos Valores: Crie uma função que receba um raio de um círculo e 
retorne a área e a circunferência. Desempacote os valores do retorno em duas variáveis 
separadas. Imprima os resultados."""

import math

def calcular_area_e_circunferencia(raio: float) -> tuple:
    area = math.pi * raio**2
    circunferencia = 2 * math.pi * raio
    return area, circunferencia

raio = 5
area, circunferencia = calcular_area_e_circunferencia(raio)
print(f"Raio: {raio}")
print(f"Área: {area:.2f}")
print(f"Circunferência: {circunferencia:.2f}")
