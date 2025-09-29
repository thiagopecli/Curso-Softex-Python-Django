"""2. Criando uma Cafeteira (Fácil) 
 
●  Classes: GraoDeCafe, Agua e Cafeteira. 
●  Classe GraoDeCafe: 
○  Método: __init__ (sem atributos). 
○  Método: moer() que imprime "Os grãos de café foram moídos.". 
●  Classe Agua: 
○  Método: __init__ (sem atributos). 
○  Método: aquecer() que imprime "A água está aquecida.". 
●  Classe Cafeteira: 
○  Atributos (Composição): grao e agua, que devem ser instâncias das classes 
GraoDeCafe e Agua. 
○  Método: __init__ que inicializa os atributos grao e agua. 
○  Método: preparar_cafe() que chama os métodos moer() do seu grao e aquecer() da 
sua agua."""

class GraoDeCafe():
    def __init__(self):
        pass

    def moer(self):
        print("Os gãos de café foram moídos.")

class Agua():
    def __init__(self):
        pass

    def aquecer(self):
        print("A agua está aquecida...")

class Cafeteria():
    def __init__(self):
        self.moer = GraoDeCafe()
        self.aquecer = Agua()
    
    def preparar_cafe(self):
        self.moer.moer()
        self.aquecer.aquecer()

cafe = Cafeteria()
cafe.preparar_cafe()