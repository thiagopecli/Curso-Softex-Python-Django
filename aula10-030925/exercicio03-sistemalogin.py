acesso = [("Pedro", "sucesso"), ("Ana", "falha"), ("Maria", "sucesso"), ("Pedro", "falha"), ("Ana", "falha")]

usuario_sucesso = set()
usuario_falha = set()

for usuario, status in acesso:
    if status == "sucesso":
        usuario_sucesso.add(usuario)
    elif status == "falha":
        usuario_falha.add(usuario)

so_falha = usuario_falha.difference(usuario_sucesso)

print(so_falha)
print(usuario_sucesso)