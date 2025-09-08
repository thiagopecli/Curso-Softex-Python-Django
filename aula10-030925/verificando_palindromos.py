"""1. Verificando Palíndromos:

Um palíndromo é uma sequência que lê o mesmo de trás para frente. Crie um programa que 
verifique se uma lista é um palíndromo. 
●  Entrada: Uma lista de elementos. 
●  Saída: True se a lista for um palíndromo, False caso contrário. """


while True:

    lista1 = input("Digite uma palavra: ")

    invertida = lista1[::-1]
    resultado = (lista1 == invertida)

    print(f"A lista {lista1} é um polindromo? {resultado}")