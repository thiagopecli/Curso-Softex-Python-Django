import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
    def __init__(self):
        self.banco_blog_conn = DatabaseConnection
        self.create_table()

    def _creat_table(self):
        self.banco_blog_conn.connect()
        self.banco_blog_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao DATATIME DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao DATATIME DEFAULT CURRENT_TIMESTAMP,
            FORENG KEY (id) REFERENCES FORENG KEY (id)
            );
        """
        )
        self.banco_blog_conn.close()
    
    def criar_postagem(self, postagem):
        self.banco_blog_conn.connect()
        try:
            self.banco_blog_conn.cursor.execute(
                """
                INSERT INTO """
            )