"""23. Autenticador de Usuário: Crie uma função autenticar(usuario, senha) que verifica se o 
usuário e a senha existem em um dicionário pré-definido. A função deve retornar True se 
a autenticação for bem-sucedida e False caso contrário. Imprima o resultado."""

def autenticar(usuario: str, senha: str) -> bool:
    usuarios = {
        "usuario1": "senha1",
        "usuario2": "senha2",
        "usuario3": "senha3"
    }
    return usuarios.get(usuario) == senha

resultado = autenticar("usuario1", "senha1")
print(f"Autenticação bem-sucedida: {resultado}")
resultado = autenticar("usuario2", "senhaErrada")
print(f"Autenticação bem-sucedida: {resultado}")