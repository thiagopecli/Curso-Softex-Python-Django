"""3. Segmento de Reta (Fácil/Médio) 
 
●  Classes: Ponto e SegmentoDeReta. 
●  Classe Ponto: 
○  Atributos: x e y. 
○  Método: __init__(x, y). 
●  Classe SegmentoDeReta: 
○  Atributos (Composição): ponto1 e ponto2, que devem ser instâncias de Ponto. 
○  Método: __init__(ponto1, ponto2). 
○  Método: calcular_comprimento() que retorna a distância entre os dois pontos. 
●  Dica: Use o módulo math e a fórmula da distância euclidiana: 
(x2 −x1 )2+(y2 −y1 )2. """

import math

class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class SegmentoDeReta:
    def __init__(self, ponto1: Ponto, ponto2: Ponto) -> None:
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def calcular_comprimento(self):
        x1 = self.ponto1.x
        y1 = self.ponto1.y
        x2 = self.ponto2.x
        y2 = self.ponto2.y
    
        distancia_x = (x2 - x1) ** 2
        distancia_y = (y2 - y1) ** 2
        soma_distancia = distancia_x + distancia_y

        comprimento = math.sqrt(soma_distancia)
        return comprimento

p1 = Ponto(x=3, y=2)
p2 = Ponto(x=7, y=5)

meu_segmento = SegmentoDeReta(ponto1=p1, ponto2=p2)
comprimento_calculado = meu_segmento.calcular_comprimento()

print(f"O comprimento do segmento de reta entre o ponto ({p1.x}, {p1.y}) e "
      f"({p2.x, p2.y}) é: {comprimento_calculado:.2f}.")