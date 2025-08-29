""" Desafio de Programação: Validação do Triângulo
Seu objetivo: Escrever um algoritmo em Python que determine se três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se para um número teste for positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número."""

print("--- Validador de Triângulo ---")
print("Por favor, forneça o comprimento dos três lados.")

# --- Obter Lado A ---
while True:
    entrada_usuario = input("Digite o valor do Lado A: ")
    # Validação manual para verificar se a entrada é um número
    if not entrada_usuario or entrada_usuario.count('.') > 1:
        print("Erro: A entrada é inválida. Tente novamente.")
        continue
    
    string_para_teste = entrada_usuario.replace('.', '', 1)

    if string_para_teste.isdigit():
        la = float(entrada_usuario)
        if la > 0:
            break  # Entrada válida, sai do loop do Lado A
        else:
            print("Erro: O valor do lado deve ser um número positivo. Tente novamente.")
    else:
        print("Erro: A entrada contém caracteres que não são números. Tente novamente.")

# --- Obter Lado B ---
while True:
    entrada_usuario = input("Digite o valor do Lado B: ")
    # Validação manual para verificar se a entrada é um número
    if not entrada_usuario or entrada_usuario.count('.') > 1:
        print("Erro: A entrada é inválida. Tente novamente.")
        continue
        
    string_para_teste = entrada_usuario.replace('.', '', 1)

    if string_para_teste.isdigit():
        lb = float(entrada_usuario)
        if lb > 0:
            break  # Entrada válida, sai do loop do Lado B
        else:
            print("Erro: O valor do lado deve ser um número positivo. Tente novamente.")
    else:
        print("Erro: A entrada contém caracteres que não são números. Tente novamente.")

# --- Obter Lado C ---
while True:
    entrada_usuario = input("Digite o valor do Lado C: ")
    # Validação manual para verificar se a entrada é um número
    if not entrada_usuario or entrada_usuario.count('.') > 1:
        print("Erro: A entrada é inválida. Tente novamente.")
        continue
        
    string_para_teste = entrada_usuario.replace('.', '', 1)

    if string_para_teste.isdigit():
        lc = float(entrada_usuario)
        if lc > 0:
            break  # Entrada válida, sai do loop do Lado C
        else:
            print("Erro: O valor do lado deve ser um número positivo. Tente novamente.")
    else:
        print("Erro: A entrada contém caracteres que não são números. Tente novamente.")


# --- Verificação Final ---
print(f"\nLados fornecidos: A = {la}, B = {lb}, C = {lc}")

# Aplica a Regra da Diferença para validar o triângulo, usando abs()
if (la > abs(lb - lc)) and (lb > abs(la - lc)) and (lc > abs(la - lb)):
    print("\nResultado: Os valores fornecidos PODEM formar um triângulo.")
else:
    print("\nResultado: Os valores fornecidos.")