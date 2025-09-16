"""Nível 4: Desafios de Lógica (Exercícios 16-20) 
 
16. Inversão de Dicionário: Crie um dicionário. Troque as chaves pelos valores e os valores 
pelas chaves. Dica: Os valores devem ser únicos para que isso funcione."""

dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario_invertido = {}
for k, v in dicionario.items():
	dicionario_invertido[v] = k
print(dicionario_invertido)