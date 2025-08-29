"""Exercício 1: Validação de E-mail Básico 

Crie um programa que simula uma validação simples de endereço de e-mail. 
1.  Defina uma variável para um e-mail correto predefinido (exemplo: "usuario@dominio.com"). 
2.  Defina uma senha de acesso. 
3.  O programa deve pedir a senha ao usuário. Use um while loop para garantir que o acesso só ocorra após a senha correta ser digitada. 
4.  Após o login, peça ao usuário para digitar um e-mail para validação. 
5.  O programa deve verificar se o e-mail digitado contém o caractere "@" e se o e-mail termina com ".com". 
6.  Use uma estrutura if para checar as duas condições. Use o operador and para combinar as verificações. 
7.  Se ambas as condições forem verdadeiras, exiba a mensagem: "E-mail válido!". Se uma ou ambas as condições forem falsas, exiba a mensagem: "E-mail inválido.". 
8.  O programa deve perguntar se o usuário quer validar outro e-mail. Se a resposta for "sim", o processo deve se repetir. Se for "não", o programa deve encerrar."""

email = "thiago@gmail.com"
senha = "R9!p2@Lz"

while True:
    email_digitado = input("Digite o email: ")
    senha_digitada = input("Digite a senha: ")

    if email_digitado == email and senha_digitada == senha:
        print("Acesso autorizado! ")
        break
    else:
        print("Acesso negado! ")
    
while True:
    validador_email = input("Digite um email para validação: ")

    if "@" in validador_email and validador_email.endswith(".com"):
        print("E-mail Válido!")  
    else:
        print("E-mail inválido!")

    continua_validador = input("Quer validar outro e-mail (s/n):")
    continua_validador_formatado = continua_validador.lower()

    if continua_validador_formatado == "s":
        continue
    else:
        break

print("Validador Encerrado...!")
