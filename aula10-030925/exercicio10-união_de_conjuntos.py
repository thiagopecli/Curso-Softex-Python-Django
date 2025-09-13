"""10. União de Conjuntos: 
Você tem dois conjuntos de clientes: clientes_premium = {'Maria', 
'Pedro', 'Ana'} e clientes_recentes = {'Ana', 'João', 'Lucas'}. Use o método .union() para 
criar um novo conjunto com todos os clientes. """

clientes_premium = {'Maria', 'Pedro', 'Ana'}
clientes_recente = {'Ana', 'João', 'Lucas'}
print(f"Clientes Premium: {clientes_premium}")
print(f"Clientes Recente: {clientes_recente}")

todos_os_clientes = clientes_premium.union(clientes_recente)
print(f"Todos os clientes: {todos_os_clientes}")