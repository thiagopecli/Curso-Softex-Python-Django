# Tipos de Operadores Relacionais - comparam valores e retornam True ou False:
# 1. Igualdade: 7 == 7 True
# 2. Diferença: 8 != 6 True
# 3. Maior que: 5 > 3 True
# 4. Menor que: 2 < 1 False
# 5. Maior ou igual a: 5 >= 5 True
# 6. Menor ou igual a: 4 <= 3 False

# Sempre que usamos operadores relacionais, o resultado é True ou False. Isso pe a base para tomar decisões no programa.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
print(a == b) # False 10 não é igual a 5
print(a != b) # True 10 é diferente de 5
print(a > b) # True 10 é maior que 5
print(a < b) # False 10 não é menor que 5
print(a >= b) # True 10 é maior ou igual a 5
print(a <= b) # False 10 não é menor ou igual a 5

# Tipos de operadores lógicos - combinam condições e retornam True ou False:
# 1. and: E - Só dá True se as duas condições forem True
# 2. or: OU - Dá True se pelo menos uma condição for True
# 3. not: NÃO - Inverte o valor lógico: True vira False, e vice-versa

# Exemplo de operadores lógicos com if e else - fazem o codigo tomar decisões com base em condições:
idade = int(input("Digite sua idade: "))
maior_de_idade = True
if idade >= 18 and maior_de_idade:
    print("Você pode tirar carteira de motorista.")
else:
    print("Você não pode tirar carteira de motorista.")

# Exemplos de operadores lógicos com elif - fazem o codigo tomar decisões com base em condições:
nota = float(input("Digite sua nota: "))
if nota >= 9:
    print("Ótimo trabalho, continue assim!")
elif nota >= 7:
    print("Bom trabalho, mas você pode melhorar.")
else:
    print("Reprovado. Você precisa estudar mais!")

# While loop com operadores lógicos - repete enquanto a condição não for verdadeira:
tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta!")
        tentativas += 1

