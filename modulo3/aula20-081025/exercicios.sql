DROP TABLE IF EXISTS alunos;
DROP TABLE IF EXISTS professor;
DROP TABLE IF EXISTS professores;
CREATE TABLE professor (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN KEY (id_professor) REFERENCES professor (id)
);

INSERT INTO professor(nome) VALUES('Anderson');
SELECT * FROM professor;
INSERT into alunos(nome, id_professor) VALUES ('João', 1);
INSERT INTO alunos(nome, id_professor) VALUES ('Mara', 1);
SELECT * FROM alunos;
SELECT alunos.NOME AS nome_aluno, professor.nome as nome_professor FROM alunos INNER JOIN professor ON alunos.id_professor = professor.id;

INSERT INTO usuarios(nome) VALUES ('Pedro'), ('Michele'), ('')

SELECT * FROM usuarios;
SELECT * FROM cursos;
SELECT * FROM usuarios_cursos;
SELECT U.nome, C.titulo FROM usuarios AS U
INNER JOIN usuarios_cursos AS UC ON UC.id_usuario = U.id
INNER JOIN cursos AS C ON UC.id_curso = C.id;