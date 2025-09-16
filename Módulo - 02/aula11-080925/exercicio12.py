"""12. Crie um dicionário onde a chave é o nome de um time e o valor é uma lista com os nomes 
de 3 jogadores. Imprima o nome do segundo jogador do segundo time."""

times = {
    "Time A": ["Jogador A1", "Jogador A2", "Jogador A3"],
    "Time B": ["Jogador B1", "Jogador B2", "Jogador B3"],
    "Time C": ["Jogador C1", "Jogador C2", "Jogador C3"]
}

print(f"Segundo jogador do Time B: {times['Time B'][1]}")