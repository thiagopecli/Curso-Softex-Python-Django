"""Faça um programa que simula um quiz simples. Pergunte qual é a capital do Brasil. O 
programa deve continuar pedindo a resposta até que o usuário acerte, usando um loop while 
e break. """

resposta_correta = "brasilia"


for resposta in resposta_correta:
    print("Qual é a Capital do Brasil?!")
    resposta = input("Resposta: ")

    if resposta == resposta_correta:
        print("Resposta Correta!")
        break
    else:
        print("Resposta incorreta. Tente novamente! ")
        continue