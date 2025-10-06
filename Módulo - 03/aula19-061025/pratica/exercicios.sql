CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
);

CREATE TABLE postagens(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagens TEXT NOT NULL,
    id_autor TEXT NOT NULL,
);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Jorge', 'Silva', 'silva@gmail.com', '1234');