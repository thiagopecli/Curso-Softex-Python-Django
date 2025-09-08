"""2. Removendo Todas as Ocorrências

Crie um programa que remova todas as ocorrências de um item específico de uma lista. Se o 
item não existir, nada acontece. 
●  Entrada: Uma lista de elementos e o item a ser removido. 
●  Saída: A lista original, mas sem o item especificado."""

lista = [1,2,3,4,5,6,7,8,9]

while True:
    remover = input("Digite o item a ser removido: ")

    try: 
        numero_para_remover = int(remover)

        if numero_para_remover in lista:
            lista.remove(numero_para_remover)
        else:
            print("O item não está na lista. ")
    
    except ValueError:
        print("Digite um número válido!")

    print(f"lista final: {lista}")