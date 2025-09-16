"""12. Diferença de Conjuntos: 
Ainda com os conjuntos do exercício 10, use o método .difference() para encontrar os clientes que são premium mas não são recentes."""

clientes_premium = {'Maria', 'Pedro', 'Ana'}
clientes_recente = {'Ana', 'João', 'Lucas'}
print(f"Clientes Premium: {clientes_premium}")
print(f"Clientes Recente: {clientes_recente}")

premium_nao_recente = clientes_premium.difference(clientes_recente)
print(f"Clientes que são premium, mas não são recentes: {premium_nao_recente}")

recentes_nao_premium = clientes_recente.difference(clientes_premium)
print(f"Clientes recentes, mas não são premium: {recentes_nao_premium}")