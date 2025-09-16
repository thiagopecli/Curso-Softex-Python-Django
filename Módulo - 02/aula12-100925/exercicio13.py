"""13. Validador de Senha: Crie uma função que receba uma senha (string) e retorne True se 
ela tiver pelo menos 8 caracteres e False caso contrário. Imprima o resultado."""

def validar_senha(senha: str) -> bool:
    return len(senha) >= 8

resultado = validar_senha("minhasenha")
print(f"A senha é válida? {resultado}")

resultado = validar_senha("curta")
print(f"A senha é válida? {resultado}")