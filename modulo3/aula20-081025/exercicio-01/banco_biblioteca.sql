CREATE TABLE autores(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao TEXT NOT NULL
);
CREATE TABLE autores_livros(
    id_autor INTEGER NOT NULL,
    id_livro INTEGER NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES autores(id),
    FOREIGN KEY (id_livro) REFERENCES livros(id)
);

INSERT INTO autores(nome, nacionalidade) VALUES ('Machado de Assis', 'Brasileiro'), ('Clarice Lispector', 'Brasileiro');
INSERT INTO livros(titulo, ano_publicacao) VALUES ('Dom Casmurro', '1899'), ('A Hora da Estrela', '1977');
INSERT INTO autores_livros(id_autor, id_livro) VALUES (1,1), (1,2);
INSERT INTO autores_livros(id_autor, id_livro) VALUES (2,1);
SELECT * FROM autores;
SELECT * FROM livros;
SELECT * FROM autores_livros;
SELECT count(autores.nome) from autores WHERE nome = 'Dom Casmurro';