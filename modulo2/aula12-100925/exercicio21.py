"""Nível Expert (Foco em try/except e Lógica Complexa) 
 
21. Validador de Entrada Numérica: Crie uma função que solicite ao usuário que digite um 
número inteiro. Use um loop e try/except para garantir que a entrada seja válida. A 
função deve retornar o número inteiro."""

def validar_entrada_inteira() -> int:
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numero = validar_entrada_inteira()
print(f"Número digitado: {numero}")
