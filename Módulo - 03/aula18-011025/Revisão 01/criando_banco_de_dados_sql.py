import sqlite3

conn = sqlite3.connect('meu_banco.db')

print("Bando de dados 'meu_banco.db' Criado com sucesso. ")

# É sempre bom fechar a conexão. 

conn.close()