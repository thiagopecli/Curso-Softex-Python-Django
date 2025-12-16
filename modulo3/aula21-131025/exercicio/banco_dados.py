import sqlite3

class DatabaseConnection:
    def __init__(self, db_nome="banco_blog.db"):
        self.db_nome = db_nome
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_nome)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()
    
    def close(self):
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None