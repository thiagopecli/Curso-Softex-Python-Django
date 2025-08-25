######## Jogo Prático: Pedra, papel e tesoura ########
# Este é um exemplo clássico que combina o módulo random, listas e o loop while para criar 
# uma experiência interativa. A lógica é simples: o computador faz uma escolha aleatória, você 
# faz a sua, e o programa decide quem vence.

    # Lista de opções
    # Usamos um loop 'While True' para que o jogo continue rodando até que o usuario decida parar.
    # Escolha aleatória do computador:
    # Solicita a escolha do usuário:
    # Verifica se a escolha do usuário é valida:
    # Exibe a escolha do computador:
    # A lógica do jogo: usando as estruturas if-elif:
    # Pergunta se o usuário quer jogar novamente:

import random

while True:
    print("\nxxXX Jogo: Pedra, Papel, Tesoura, Lagarto e Spock! XXxx ")
    print("|Para encerrar, digite 'sair'|")

    opcoes = ("pedra", "papel", "tesoura", "lagarto", "spock")
    computador = random.choice(opcoes)
    jogador = input("Esolha uma das opções: Pedra, Papel, Tesoura, Lagarto ou Spock: ").lower()

    if jogador == 'sair':
        print("Saindo...")
        break
    elif jogador not in opcoes:
        print("Opção invalida, digite uma opção válida: ")
        continue

    print(f"O computador escolheu: {computador}")

    if jogador == computador:
        print("Deu Empate, jogue novamente!")
    elif jogador == "tesoura" and computador == "papel":
        print("Você venceu, tesoura corta papel!")
    elif jogador == "papel" and computador == "pedra":
        print("Você venceu, papel cobre pedra!")
    elif jogador == "pedra" and computador == "lagarto":
        print("Você venceu, pedra esmaga lagarto!")
    elif jogador == "lagarto" and computador == "spock":
        print("Você venceu, lagarto envenena spock!")
    elif jogador == "spock" and computador == "tesoura":
        print("Você venceu, spock derrete tesoura")
    elif jogador == "tesoura" and computador == "lagarto":
        print("Você venceu, tesoura decapita lagarto")
    elif jogador == "lagarto" and computador == "papel":
        print("Você venceu, lagarto come papel")
    elif jogador == "papel" and computador == "spock":
        print("Você venceu, papel refuta spock")
    elif jogador == "spock" and computador == "pedra":
        print("Você venceu, Spock vaporiza pedra")
    elif jogador == "pedra" and computador == "tesoura":
        print("Você venceu, pedra quebra tesoura")
    elif computador == "tesoura" and jogador == "papel":
        print("O computador venceu, tesoura corta papel!")
    elif computador == "papel" and jogador == "pedra":
        print("O computador venceu, papel cobre pedra!")
    elif computador == "pedra" and jogador == "lagarto":
        print("O computador venceu, pedra esmaga lagarto!")
    elif computador == "lagarto" and jogador == "spock":
        print("O computador venceu, lagarto envenena spock!")
    elif computador == "spock" and jogador == "tesoura":
        print("O computador venceu, spock derrete tesoura!")
    elif computador == "tesoura" and jogador == "lagarto":
        print("O computador venceu, tesoura decapita lagarto!")
    elif computador == "lagarto" and jogador == "papel":
        print("O computador venceu, lagarto come papel!")
    elif computador == "papel" and jogador == "spock":
        print("O computador venceu, papel refuta spock!")
    elif computador == "spock" and jogador == "pedra":
        print("O computador venceu, spock vaporiza pedra!")
    elif computador == "pedra" and jogador == "tesoura":
        print("O computador venceu, pedra quebra tesoura!")
    
    jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
    
    if jogar_novamente != "s":
        break

print("Obrigado por jogar!")