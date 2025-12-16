######## Classificador de Triangulos ########

# 6. Classificador de Triângulos (if-elif-else): 
# ○ Peça ao usuário para digitar o comprimento de três lados de um triângulo. 
# ○ Use a lógica condicional para classificar o triângulo em: 
# ■ "Equilátero" (todos os lados iguais) 
# ■ "Isósceles" (dois lados iguais) 
# ■ "Escaleno" (todos os lados diferentes) 

print("\n --- Classificador de Triângulos --- ")

lado_a = float(input("Digite o comprimento do lado A: "))
lado_b = float(input("Digite o comprimento do lado B: "))
lado_c = float(input("Digite o comprimento do lado C: "))

if lado_a == lado_b == lado_c:
    print("O triângulo é Equilátero.")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")