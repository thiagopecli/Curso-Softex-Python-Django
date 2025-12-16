CREATE TABLE alunos (
    id INTEGER PRIMARY  KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos (nome, idade) VALUES('João', 20);
INSERT INTO alunos (nome, idade) VALUES('Telma', 50);
INSERT INTO alunos (nome, idade) VALUES('', 50);

SELECT * FROM alunos;
SELECT nome, idade FROM alunos;
SELECT * FROM alunos WHERE idade = 20;
UPDATE alunos SET idade = 21 WHERE nome = 'João';
DELETE FROM alunos WHERE id = 3;


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

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Jorge', 'Silva', 'silva@gmail.com', '1234')