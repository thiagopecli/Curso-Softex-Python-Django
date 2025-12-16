# Crie um programa que pede ao usuário para digitar um número e usa um loop for para 
# imprimir a tabuada desse número de 1 a 10. 

num = int(input("Digite o número: "))

for i in range(1, 11):
    print(f"{num} x {i} = {i * num}")