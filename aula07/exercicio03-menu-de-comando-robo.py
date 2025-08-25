"""
Exercício 3: Menu de Comandos para um Robô

Crie um programa que simula o controle de um robô simples com um menu de comandos.
1. O robô pode estar em uma posição inicial (você pode usar uma variavel para isso, por exemplo, a posição 0.)
2. O programa deve exibir um menu com as seguintes opções: 1 Avançar, 2 Recuar, 3 Status, 4 Desligar.
3. Peça ao usuario para escolher um comando.
4. Com base na escolha, execute a ação correspondente:
    Avançar: Adicione um valor à posição do robô;
    Recuar: Subtrai um valor da posição robô;
    Status: Mostre a posição atual do robô;
    Desligar: Encerra o programa.
5.O menu deve continuar aparecendo após cada comando, até que o usuário escolha a opção "Desligar".
6. Se o usuário digitar um comando inválido, exiba uma mensagem de erro.

"""
posicao_inicial = 0


while True:
    print("n\ Menu: 1- Avançar, 2- Recuar, 3- Status, 4- Desligar")

    comando = int(input("Digite o comando desejado: "))

    if comando == 1:
        valor = int(input("Digite o valor para avançar: "))
        posicao_inicial += valor
        print(f"O robô avançou {valor} casas.")
    elif comando == 2:
        valor = int(input("Digite o valor para recuar: "))
        posicao_inicial -= valor
        print(f"O robô recuou {valor} casas.")
    elif comando == 3:
        print(f"A posição atual do robô é: {posicao_inicial}")
    elif comando == 4:
        print("Desligando o robô. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente!")
