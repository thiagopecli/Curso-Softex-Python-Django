"""
Exercício 4: Coletor de Dados Robusto 

Crie um programa que colete números de usuário e os armazene em uma lista. O programa 
deve continuar pedindo números até que o usuário digite -1 para parar. Ele deve validar a 
entrada para garantir que o que foi digitado é realmente um número antes de prosseguir. 
Apenas os números entre 0 e 100 devem ser considerados válidos e adicionados à lista. Ao 
final, imprima a soma dos números válidos e a lista dos números coletados. 

● Entrada: Vários valores digitados pelo usuário, um de cada vez. 
● Saída: A soma dos números válidos e a lista dos números coletados. 
"""

while True:
    print("Para sair digite -1")
    usuario = input("Digite um número: ")
    lista_nova = []
    print(usuario)