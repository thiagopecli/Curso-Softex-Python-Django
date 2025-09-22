"""Exercício 7: Calculadora de Retângulos 
 
Crie uma classe Retangulo que é inicializada com base e altura. Crie dois 
métodos: 
1.  calcular_area(): deve retornar o cálculo base * altura. 
2.  calcular_perimetro(): deve retornar o cálculo 2 * (base + altura). 
Crie um retângulo, chame os dois métodos e imprima os resultados que eles 
retornam."""

# class Retangulo():
#     def __init__(self, base:float, altura:float) -> None:
#         self.base = base
#         self.altura = altura

#     def calcular_area(self) -> float:
#         return self.base * self.altura
    
#     def calcular_perimetro(self) -> float:
#         return 2 * (self.base + self.altura)

# meu_retangulo = Retangulo(base=15,altura=20)
# area_calculada = meu_retangulo.calcular_area()
# perimetro_calculado = meu_retangulo.calcular_perimetro()

# print(f"A área calculada é: {area_calculada:.2f}.")
# print(f"O perimetro calculado é: {perimetro_calculado:.2f}.")
################################################################################

class Retangulo():
    def __init__(self, base:float, altura:float) -> None:
        self.base = base
        self.altura = altura
    def calcular_area(self) -> float:
        return self.base * self.altura
    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)
meu_retangulo = Retangulo(base=10, altura=20)
area_calculada = meu_retangulo.calcular_area()
perimetro_calculado = meu_retangulo.calcular_perimetro()

print(f"A área calculada é: {area_calculada}. ")
print(f"O perimetro calculado é: {perimetro_calculado}. ")