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

lista = []
contador = 0

while True:
    print("Para sair digite -1")
    usuario = input("Digite um número: ")

    if usuario == "-1":
        print("Saindo...")
        break

    if usuario.isdigit() or usuario.startswith("-") and usuario[1:].isdigit():
        numero = int(usuario)

        if 0 <= numero <= 100:
            lista.append(numero)
            contador += numero
        else:
            print("Digite um numero entre 0 e 100!")
    else:
        print("Digite apenas números.")

print(f"Soma de todos os números: {contador}.")
print(f"Lista: {lista}")