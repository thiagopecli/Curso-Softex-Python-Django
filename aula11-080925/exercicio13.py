"""13. Crie um dicionário que use tuplas como chaves. As chaves devem ser coordenadas (x, y) 
e os valores, o nome de um local. Peça ao usuário para digitar as coordenadas e imprima 
o local."""

locais = {
    (0, 0): "Origem",
    (1, 0): "Ponto A",
    (0, 1): "Ponto B",
    (1, 1): "Ponto C"
}

coordenadas = input("Digite as coordenadas (x, y): ")
coordenadas = tuple(map(int, coordenadas.split(",")))

if coordenadas in locais:
    print(f"Local encontrado: {locais[coordenadas]}")
else:
    print("Local não encontrado.")