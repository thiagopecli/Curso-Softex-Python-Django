"""
Exercicio 02 - Validação e Formatação de Telefone:

Crie um programa que recebe um número de telefone com 11 dígitos.
1. O número é considerado inválido se tiver 3 ou mais digitos iguais.
2. O programa devve verificar se o número tem 11 digitos e se todos os caracteres são números.
3. Se o número for válido, o programa deve formata-lo para padrão (xx) xxxxx-xxxx.
4. O programa deve imprimir o número formatado ou a mensagem de erro correspondente.

"""


while True:
    numero_telefone = input("Digite o número de telefone: ")

    if numero_telefone.isdigit() and len(numero_telefone) == 11:
        print(f"({numero_telefone[:2]}) {numero_telefone[2:7]}-{numero_telefone[7:]}")
        break
    elif len(numero_telefone) < 11:
        print("Menos de 11 digitos.")
        break
    else:
        print("Entrada inválida!")
        break
