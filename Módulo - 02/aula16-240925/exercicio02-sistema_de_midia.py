"""2. Nível Médio: Sistema de Mídia 
 
Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. 
Adicione um método exibir() que imprime o título e a duração.

Crie duas classes filhas, Musica e Video, que herdam de Midia: 
●  Musica deve ter um atributo adicional artista e sobrescrever o método 
exibir() para incluir o nome do artista. 
●  Video deve ter um atributo adicional resolucao e sobrescrever o método 
exibir() para incluir a resolução. 
No script principal, crie um dicionário para organizar sua coleção de mídias, 
usando as chaves 'musicas' e 'videos'. Crie objetos de Musica e Video e os 
adicione a suas respectivas listas dentro do dicionário. Por fim, itere sobre 
as listas e chame o método exibir() para cada item, demonstrando o polimorfismo
de forma organizada."""

class Midia():
    def __init__(self, titulo:str, duracao:int):
        self.titulo = titulo
        self.duracao = duracao
    def exibir(self):
        print(f"Titulo: {self.titulo}. Duraçao: {self.duracao} minutos")

class Musica(Midia):
    def __init__(self, titulo:str, duracao:int, artista:str):
        super().__init__(titulo, duracao)
        self.artista = artista
    def exibir(self):
        print((f"Titulo: {self.titulo}. Artista: {self.artista}. Duração: "
              f"{self.duracao} minutos. "))

class Video(Midia):
    def __init__(self, titulo:str, duracao:int, resolucao:str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
    def exibir(self):
        print((f"Titulo: {self.titulo}. Duração: {self.duracao} minutos. "
               f"Resolução: {self.resolucao} pixels."))
        
colecao = {
    'musicas': [],
    'videos': []
}

musica = Musica("Exemplo 02", 3, "José")
video = Video("Exemplo 03", 3, "1080")

colecao['musicas'].append(musica)
colecao["videos"].append(video)

for tipo_midia, lista_de_midia in colecao.items():
    for item in lista_de_midia:
        item.exibir()