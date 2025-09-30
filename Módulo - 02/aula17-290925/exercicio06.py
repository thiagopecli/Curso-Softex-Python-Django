"""6. Playlist de Músicas (Médio) 
 
●  Classes: Musica e Playlist. 
●  Classe Musica: 
○  Atributos: titulo e artista. 
○  Método: __init__(titulo, artista). 
●  Classe Playlist: 
○  Atributo (Composição): musicas, que deve ser uma lista vazia. 
○  Método: __init__ que inicializa a lista musicas. 
○  Método: adicionar_musica(musica) que recebe um objeto Musica e o adiciona 
na lista. 
○  Método: remover_musica(musica) que remove um objeto Musica da lista. 
○  Método: tocar_playlist() que itera sobre a lista de músicas e imprime 
"Tocando [título] de [artista]". """

class Musica:
    def __init__(self, titulo, artista) -> None:
        self.titulo = titulo
        self.artista = artista
    
class Playlist:
    def __init__(self) -> None:
        self.musica = []

    def adicionar_musica(self, nova_musica):
        nova_musica = Musica(titulo=nova_musica, artista=nova_musica)
        self.musicas.append(nova_musica)
        