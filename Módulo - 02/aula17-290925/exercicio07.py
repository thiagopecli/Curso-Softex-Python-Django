"""7. Carro com Motor e Rodas (Médio) 
 
●  Classes: Motor, Roda e Carro. 
●  Classe Motor: 
○  Método: __init__ (sem atributos). 
○  Método: ligar() que imprime "Motor ligado.". 
●  Classe Roda: 
○  Método: __init__ (sem atributos). 
○  Método: girar() que imprime "A roda está girando.". 
●  Classe Carro: 
○  Atributos (Composição): motor e rodas (uma lista). 
○  Método: __init__ que inicializa o motor e cria uma lista com 4 instâncias 
de Roda. ○  Método: ligar_carro() que chama o método ligar() do motor e, em 
seguida, itera sobre a lista rodas para chamar o método girar() de cada uma."""

class Motor:
    def __init__(self) -> None:
        pass
    def ligar(self):
        print("O motor foi ligado!")

class Roda:
    def __init__(self) -> None:
        pass
    
    def girar(self):
        print("A roda está girando!")

class Carro:
    def __init__(self) -> None:
        self.motor = Motor()
        self.rodas = [Roda() for _ in range(4)]
    
    def ligar_carro(self):
        print("Ligando o carro...")
        self.motor.ligar()

        print("Verificando rodas! ")
        for roda in self.rodas:
            roda.girar()
        print("Carro pronto! ")

