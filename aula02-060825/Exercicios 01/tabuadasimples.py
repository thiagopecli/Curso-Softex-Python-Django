# Tabuada Simples 
# ● Peça um número ao usuário. 
# ● Use um while para imprimir a tabuada desse número, de 1 a 10. 
# ○ Exemplo: 5 x 1 = 5, 5 x 2 = 10, etc. 

numero = int(input("Digite um número para ver a tabuada: "))
contador = 1

print(f"Tabuada do {numero}:")
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
print("Tabuada finalizada!")