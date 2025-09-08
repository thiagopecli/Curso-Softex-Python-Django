"""3. Encontrando o Segundo Maior Valor

Encontre o segundo maior número em uma lista de números. O programa não pode usar o 
método .sort() da lista. 
●  Entrada: Uma lista de números inteiros. 
●  Saída: O segundo maior número. """

lista_de_numeros = [10,55,20,25,8,5,105]


maior = float('-inf')
segundo_maior = float('-inf')

for numero_atual in lista_de_numeros:
    if numero_atual > maior:
        segundo_maior = maior
        maior = numero_atual

    elif numero_atual > segundo_maior and numero_atual != maior:
        segundo_maior = numero_atual

if segundo_maior == float('-inf'):
    print("Não foi encontrado um segundo maior valor na lista.")
else:
    print(f"O maior numero da lista é: {maior}")
    print(f"O segundo maior numero é: {segundo_maior}")