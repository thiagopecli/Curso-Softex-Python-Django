"""Exercício 8: Um Carro que Anda 
 
Crie uma classe Carro com os atributos modelo e nivel_combustivel (começando 
com 0). 
1.  Crie um método para abastecer(litros) que aumenta o nível de combustível. 
2.  Crie um método dirigir(distância) que consome combustível (ex: 1 litro a 
cada 10 km). O método deve verificar se há combustível suficiente para a viagem.
Se houver, diminua o combustível e avise que o carro andou. Se não, avise que 
não há combustível."""

class Carro():
    def __init__(self, modelo:str) -> None:
        self.modelo = modelo
        self.nivel_combustivel = 0
    def abastecer(self, litros:float) -> None:
        if litros > 0:
            self.nivel_combustivel += litros
            print(f"O carro foi abastecido com {litros:.2f} litros.")
        else:
            print("Erro: A quantidade de litros deve ser positivo.")
    def dirigir(self, distancia: float) -> None:
        if distancia <= 0:
            print(f"Erro: A distancia a ser percorrida deve ser positiva. ")
            return
        consumo_necessario = distancia / 10.0
        
        if self.nivel_combustivel >= consumo_necessario:
            self.nivel_combustivel -= consumo_necessario
            print(f"O {self.modelo} andou {distancia} km.")
        else:
            print((
                f"Não há combustível suficiente para o {self.modelo} andar" 
                f" {distancia} km."))
    
    def mostrar_combustivel(self) -> None:
        """Exibe o nível atual de combustível."""
        print((
            f"O nível de combustível do {self.modelo} é: "
            f"{self.nivel_combustivel:.1f} litros."))

fusca = Carro("Fusca")
fusca.mostrar_combustivel()

print("\n- Tentando dirigir sem combustível -")
fusca.dirigir(50)

print("\n- Abastecendo o carro -")
fusca.abastecer(20)
fusca.mostrar_combustivel()

print("\n- Dirigindo com combustível -")
fusca.dirigir(150)
fusca.mostrar_combustivel()

print("\n- Tentando dirigir mais do que o possível -")
fusca.dirigir(60)
fusca.mostrar_combustivel()