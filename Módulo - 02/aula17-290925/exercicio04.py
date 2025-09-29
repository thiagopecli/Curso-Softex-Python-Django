"""4. Dispositivos de um Computador (Fácil/Médio) 
 
●  Classes: Teclado, Mouse, Monitor e Computador. 
●  Classes Teclado, Mouse, Monitor: 
○  Método: __init__ (sem atributos). 
○  Método: ligar() que imprime uma mensagem indicando que o dispositivo está ligado 
(ex: "O teclado foi ativado."). 
●  Classe Computador: 
○  Atributos (Composição): teclado, mouse e monitor, que devem ser instâncias das 
classes correspondentes. 
○  Método: __init__ que inicializa os três atributos. 
○  Método: ligar_computador() que chama o método ligar() de cada um dos seus 
dispositivos. """

class Teclado:
    def __init__(self) -> None:
        pass
    def ligar_teclado(self):
        print("O teclado foi ligado.")

class Mouse:
    def __init__(self) -> None:
        pass
    def ligar_mouse(self):
        print("O mouse foi ligado.")

class Monitor:
    def __init__(self) -> None:
        pass
    def ligar_monitor(self):
        print("O monitor foi ligado.")

class Computador:
    def __init__(self) -> None:
        self.ligar_teclado = Teclado()
        self.ligar_mouse = Mouse()
        self.ligar_monitor = Monitor()
    def ligar_computador(self):
        self.ligar_teclado.ligar_teclado()
        self.ligar_mouse.ligar_mouse()
        self.ligar_monitor.ligar_monitor()
        print("Os componetes foram verificados, o compuatdor foi ligado com sucesso!")

teclado = Teclado()
mouse = Mouse()
monitor = Monitor()
computador = Computador()

computador.ligar_computador()