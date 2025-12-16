# Calculadora de média (While e if):
# Crie um programa que peça notas ao usuario:
# Use um while para continuar até que o usuario digite -1:
# Calcule e imprima a média das notas:

# Iniciando as variáveis:
soma_notas = 0
contador_notas = 0

print("=== Calculadora de Média ===")
print("Digite as notas dos alunos (digite -1 para encerrar e calcular a média)")

# Loop para iniciar a coleta de notas:
while True:
    nota = float(input("Digite a nota do aluno: "))
    
    # Verifica se o usuario quer sair:
    if nota == -1:
        break
    
    # Verifica se a nota é válida:
    if nota < 0 or nota > 10:
        print("Nota invalida. Digite uma nota entre 0 e 10.")
        continue
    
    # Adiciona a nota a soma e incrementa contador:
    soma_notas += nota
    contador_notas += 1
    print(f"Nota {nota} adicionada. Total de notas: {contador_notas}")

# Calcular e exibir a média (após sair do loop):
if contador_notas > 0:
    media = soma_notas / contador_notas
    print(f"\n=== Resultado ===")
    print(f"Total de notas inseridas: {contador_notas}")
    print(f"Soma das notas: {soma_notas}")
    print(f"Média das notas: {media:.2f}")
    
    # Classificar a média:
    if media >= 9:
        print("Classificação: Excelente!")
    elif media >= 7:
        print("Classificação: Bom!")
    elif media >= 5:
        print("Classificação: Regular")
    else:
        print("Classificação: Insuficiente")
else:
    print("Nenhuma nota foi inserida!")