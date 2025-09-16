"""Nível Intermediário (Foco em return, loops e if com tipagem) 
 
8.  Verificador de Login: Crie uma função que receba um nome de usuário e uma senha. Se 
o nome for "admin" e a senha for "12345", retorne "Acesso concedido". Caso contrário, 
retorne "Acesso negado". Use tipagem para os parâmetros e o retorno."""

def verificar_login(username: str, password: str) -> str:
    if username == "admin" and password == "12345":
        return "Acesso concedido"
    else:
        return "Acesso negado"
resultado = verificar_login("admin", "12345")
print(resultado)  # Saída: Acesso concedido
resultado = verificar_login("user", "senha")
print(resultado)  # Saída: Acesso negado