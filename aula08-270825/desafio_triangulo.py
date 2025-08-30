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

################################################################################################

print("--- Validador de Triângulo ---")
print("Digite a medida dos três lados.")

                # --- Lado A --- #

while True:
    entrada_valor = input("Digite a medida do Lado A: ")
    
    if not entrada_valor or entrada_valor.count('.') > 1:
        print("Erro: A entrada é inválida.")
        continue
    
    string_teste = entrada_valor.replace('.', '', 1)

    if string_teste.isdigit():
        lado_a = float(entrada_valor)
        if lado_a > 0:
            break
        else:
            print("Erro: O valor do lado deve ser um número positivo.")
    else:
        print("Erro: A entrada não contém números.")

                # --- Lado B --- #

while True:
    entrada_valor = input("Digite a medida do Lado B: ")

    if not entrada_valor or entrada_valor.count('.') > 1:
        print("Erro: A entrada é inválida.")
        continue
        
    string_teste = entrada_valor.replace('.', '', 1)

    if string_teste.isdigit():
        lado_b = float(entrada_valor)
        if lado_b > 0:
            break
        else:
            print("Erro: O valor do lado deve ser um número positivo.")
    else:
        print("Erro: A entrada não contém números.")

                # --- Lado C --- #

while True:
    entrada_valor = input("Digite a medida do Lado C: ")
    
    if not entrada_valor or entrada_valor.count('.') > 1:
        print("Erro: A entrada é inválida.")
        continue
        
    string_teste = entrada_valor.replace('.', '', 1)

    if string_teste.isdigit():
        lado_c = float(entrada_valor)
        if lado_c > 0:
            break
        else:
            print("Erro: O valor do lado deve ser um número positivo.")
    else:
        print("Erro: A entrada não contém números.")


print(f"\nLados digitados: A = {lado_a}, B = {lado_b}, C = {lado_c}")

if (lado_a > abs(lado_b - lado_c)) and (lado_b > abs(lado_a - lado_c)) and (lado_c > abs(lado_a - lado_b)):
    print("\nResultado: As medidas digitadas formam um triângulo.")
else:
    print("\nResultado: As medidas digitadas não formam um triângulo.")