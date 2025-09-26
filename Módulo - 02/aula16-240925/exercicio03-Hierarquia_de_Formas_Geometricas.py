"""3. Nível Médio/Avançado: Hierarquia de Formas Geométricas 
 
Crie uma classe base FormaGeometrica com um construtor para cor e um método 
calcular_area() que não faz nada. 
Crie uma classe Retangulo que herda de FormaGeometrica e tem atributos para 
largura e altura. A classe deve sobrescrever o método calcular_area(). 
Crie uma classe Quadrado que herda de Retangulo. O construtor deve receber 
apenas o lado e passar esse mesmo valor para largura e altura da classe pai. 
O encapsulamento deve ser aplicado aos atributos de dimensão. 

No script principal, crie uma tupla com um objeto de Retangulo e um objeto de 
Quadrado. Crie uma função chamada calcular_soma_areas() que recebe essa tupla,
itera sobre ela e soma a área de todas as formas. A função deve chamar o método
calcular_area() de forma polimórfica para cada objeto, exibindo a soma total 
no final."""

class FormaGeometria:
    def __init__(self, cor:str) -> None:
        self.cor = cor

    def calcular_area(self) -> float:
        raise NotImplementedError

class Retangulo(FormaGeometria):
    def __init__(self, cor: str, largura:float, altura:float) -> None:
        super().__init__(cor)
        self._largura = largura
        self._altura = altura

    def calcular_area(self) -> float:
        return self._largura * self._altura
    
class Quadrado(Retangulo):
    def __init__(self, cor: str, lado:float) -> None:
        super().__init__(cor, largura=lado, altura=lado)

def calcular_soma_areas(formas: tuple) -> None:
    soma_total = 0
    print("... Calculando área ...")

    for forma in formas:
        area = forma.calcular_area()
        soma_total += area
        print((f"A área de um {type(forma).__name__} de cor {forma.cor} é:" 
              f"{area:.2f}."))
    print(f"A soma das áreas de todas as formas é: {soma_total:.2f}.")

retangulo1 = Retangulo(cor="azul", largura=10, altura=5)
quadrado1 = Quadrado(cor="Branco", lado=7)

minha_formas = (retangulo1, quadrado1)
calcular_soma_areas(minha_formas)