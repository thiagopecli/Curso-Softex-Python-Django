"""Exercício 11: Biblioteca de Livros 
 
Crie duas classes: Livro e Biblioteca. 
1.  A classe Livro terá atributos título e autor. 
2.  A classe Biblioteca terá um atributo acervo, que começa como uma lista 
    vazia []. 
3.  A Biblioteca deve ter dois métodos: 
○  adicionar_livro(livro): recebe um objeto Livro e o adiciona à lista acervo. 
○  listar_livros(): percorre a lista acervo e imprime o título e o autor de 
    cada livro. 
Crie uma biblioteca, crie alguns objetos Livro e adicione-os à biblioteca. 
    Depois, liste os livros."""

class Livro:
    def __init__(self, titulo:str, autor:str) -> None:
        self.titulo = titulo
        self.autor = autor
class Biblioteca:
    def __init__(self) -> None:
        self.acervo = []
    def adicionar_livros(self, livro: Livro):
        self.acervo.append(livro)
        print(f"-> O livro '{livro.titulo}' foi adicionado a biblioteca.")
    def listar_livros(self):
        print("\n---- Livros da Biblioteca ---")
        if not self.acervo:
            print("A biblioteca está vazia.")
        else:
            for livro in self.acervo:
                print(f"- Titulo: {livro.titulo}, Autor: {livro.autor}.")
        print("---------------------------")

biblioteca_da_cidade = Biblioteca()
biblioteca_da_cidade.listar_livros()

livro1 = Livro("O senhor dos aneis", "J.R.R. Tolkien")
livro2 = Livro("O Guia do Mochileiro das Galaxias", "Douglas Adams")
livro3 = Livro("Duna", "Frank Herbert")

biblioteca_da_cidade.adicionar_livros(livro1)
biblioteca_da_cidade.adicionar_livros(livro2)
biblioteca_da_cidade.adicionar_livros(livro3)

biblioteca_da_cidade.listar_livros()