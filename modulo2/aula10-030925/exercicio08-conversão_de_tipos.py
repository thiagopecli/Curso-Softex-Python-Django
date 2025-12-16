"""Nível Médio (Exercícios 8 a 14) 
8.  Conversão de Tipos: Crie uma lista cidades_lista = ['Paris', 'Londres', 'Tóquio']. Converta 
essa lista para uma tupla. Depois, converta a tupla de volta para uma lista e adicione 'Nova York'."""

cidades_lista = ['paris', 'londres', 'tóquio']
print(f"Lista de cidades: {cidades_lista} (Tipo: {type(cidades_lista)})")

cidades_tuplas = tuple(cidades_lista)
print(f"Lista de cidades convertida para tupla: {cidades_tuplas} (Tipo: {type(cidades_tuplas)})")

cidades_lista_modificada = list(cidades_tuplas)
cidades_lista_modificada.append('nova york')
print(f"Lista de cidades modificada: {cidades_lista_modificada} (Tipo: {type(cidades_lista_modificada)})")