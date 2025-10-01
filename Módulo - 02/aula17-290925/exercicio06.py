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
    def __init__(self, titulo:str, artista:str) -> None:
        self.titulo = titulo
        self.artista = artista
    
    def __str__(self) -> str:
        return f"'{self.titulo}' de '{self.artista}'. "
    
class Playlist:
    def __init__(self) -> None:
        self.musicas = []

    def adicionar_musica(self, nova_musica:Musica):
        self.musicas.append(nova_musica)
        print(f"A música {nova_musica} foi adicionada a lista com sucesso. ")
    
    def remover_musica(self, musica_a_remover):
        if musica_a_remover in self.musicas:
            self.musicas.remove(musica_a_remover)
            print(f"A musica '{musica_a_remover.titulo}' foi removida.")
        else:
            print(f"A musica '{musica_a_remover.titulo}' não foi encontrada.")
    
    def tocar_playlist(self):
        if not self.musicas:
            print("A playlist está vazia. ")
        else:
            for musica in self.musicas:
                print(f"Tocando: '{musica.titulo}' de '{musica.artista}'. ")

musica1 = Musica(titulo="Amor de Jó", artista="Abraão")
musica2 = Musica(titulo="Amor de Josefa", artista="Isaque")
musica3 = Musica(titulo="Amor de clotilde", artista="Roniere")

minha_playlist = Playlist()

minha_playlist.adicionar_musica(musica1)
minha_playlist.adicionar_musica(musica2)
minha_playlist.adicionar_musica(musica3)

minha_playlist.tocar_playlist()

minha_playlist.remover_musica(musica2)

minha_playlist.tocar_playlist()