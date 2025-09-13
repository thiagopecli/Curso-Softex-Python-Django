"""11. Interseção de Conjuntos: 
Usando os mesmos conjuntos do exercício anterior, use o 
método .intersection() para encontrar os clientes que são tanto premium quanto 
recentes."""

clientes_premium = {'Maria', 'Pedro', 'Ana'}
clientes_recente = {'Ana', 'João', 'Lucas'}
print(f"Clientes Premium: {clientes_premium}")
print(f"Clientes Recente: {clientes_recente}")

clientes_premium_e_recentes = clientes_premium.intersection(clientes_recente)
print(f"Clientes que são Premium e Recentes: {clientes_premium_e_recentes}")