import sqlite3

conn = sqlite3.connect('banco_blog.db')

print("Bando de dados 'banco_blog.db' Criado com sucesso. ")

# É sempre bom fechar a conexão. 

conn.close()