"""Crie um programa que solicita ao usuário um número e, em seguida, usa um loop while para 
calcular a soma de todos os números de 1 até o número digitado. """

# --- Calculadora de Soma com 'while' ---


# 1. SOLICITAR O NÚMERO
numero_limite = int(input("Digite um número inteiro positivo: "))

# 2. VALIDAR A ENTRADA
if numero_limite < 1:
        print("Erro: Por favor, digite um número maior que zero.")
else:
    # 3. INICIALIZAR AS VARIÁVEIS
    soma_total = 0
    contador = 1 # Começamos a somar a partir do 1

    # 4. CRIAR O LOOP 'WHILE'
    # O loop continua enquanto o contador não ultrapassar o número limite
    while contador <= numero_limite:
        # 5. EXECUTAR A SOMA
        soma_total = soma_total + contador # (Forma curta de escrever: soma_total += contador)

        # 6. INCREMENTAR O CONTADOR (Passo crucial para evitar loop infinito!)
        contador = contador + 1 # (Forma curta de escrever: contador += 1)
    # 7. EXIBIR O RESULTADO FINAL
    print(f"A soma de todos os números de 1 até {numero_limite} é {soma_total}.")