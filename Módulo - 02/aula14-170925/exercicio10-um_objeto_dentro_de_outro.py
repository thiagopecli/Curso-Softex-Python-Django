"""Exercício 10: Um Objeto Dentro de Outro 
 
Crie duas classes: Motor e Carro. 
1.  A classe Motor terá um atributo potencial. 
2.  A classe Carro terá modelo. Ao criar um Carro, ele deve também criar um 
objeto Motor e guardá-lo como um de seus atributos (ex: self.motor = Motor
    (100)). 
Crie um método no Carro chamado exibir_potencia que imprime a potência do seu 
    motor."""

class Motor:
    def __init__(self, potencia:int) -> None:
        self.potencia = potencia
class Carro:
    def __init__(self, modelo: str, potencia_motor:int) -> None:
        self.modelo = modelo
        self.motor = Motor(potencia=potencia_motor)

    def exibir_potencia(self):
        print((
            f" A potência do motor do {self.modelo} é de "
            f"{self.motor.potencia} cavalos."
        ))

fusca = Carro("Fusca", 80)
fusca.exibir_potencia()

ferrari = Carro("Ferrari", 720)
ferrari.exibir_potencia()