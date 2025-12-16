"""7.  Usando o dicionário do exercício anterior, imprima apenas os nomes. Depois, imprima 
apenas as idades."""

pessoas = {
    "Ana": 28,
    "Bruno": 34,
    "Carla": 22,
    "Daniel": 45
}

print("Nomes:")
for nome in pessoas.keys():
    print(nome)

print("\nIdades:")
for idade in pessoas.values():
    print(idade)