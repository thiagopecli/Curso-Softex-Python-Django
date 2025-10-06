import sqlite3

conn = sqlite3.connect('exercicios.db')

print("Bando de dados 'exercicios.db' Criado com sucesso. ")

# É sempre bom fechar a conexão. 

conn.close()