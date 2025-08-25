# Tipos de variaveis: 
inteiro = 10
string = "nome"
flutuante = 10.1
booleano = True

# Declarando variaveis e imprimindo o valor:

nome = "Thiago"
print(nome)

# Solicitando ao usuario que ele insira as informações no terminal:

nome = input("Digite seu nome: ")
print("Meu nome é: ", nome)

# Ajustando idade:

idade = int(input("Digite sua idade:"))
idade_ajustada = int(idade) + 10
print(f"Minha idade ajustada é: {idade_ajustada}")

# Declarando mais de uma informação pelo terminal:

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo: ")

print(f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}")

# Declarando Operadores:
numero = 10
operador = 5
soma = numero + operador
subtracao = numero - operador
multiplicacao = numero * operador
divisao = numero / operador
divisao_int = numero // operador
resto_da_divisao = numero % operador
potencia = numero ** operador
comparacao = numero == operador

print(f"Soma: {numero} + {operador} = {soma}\nSubtração: {numero} - {operador} = {subtracao}\nMultiplicação: {numero} * {operador} = {multiplicacao}\nDivisão: {numero} / {operador} = {divisao}\nDivisão Inteira: {numero} // {operador} = {divisao_int}\nResto da Divisão: {numero} % {operador} = {resto_da_divisao}\nPotência: {numero} ** {operador} = {potencia}\nComparação: {numero} == {operador} = {comparacao}")
print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao}\nDivisão: {divisao}\nDivisão Inteira: {divisao_int}\nResto da Divisão: {resto_da_divisao}\nPotência: {potencia}\nComparação: {comparacao}")

# Comparador de senha pelo metodo booleano:
email = input("Digite seu email: ")
senha1 = input("Digite sua senha: ")
senha2 = input("Digite novamente: ")

confirmacao = senha1 == senha2
if confirmacao:
    print("Senha confirmada com sucesso!")
else:
    print("As senhas não conferem. Tente novamente! ")
print(confirmacao)
