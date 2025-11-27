import sqlite3

conn = sqlite3.connect('banco.db')

print("Bando de dados 'banco.db' Criado com sucesso. ")

# É sempre bom fechar a conexão. 

conn.close()