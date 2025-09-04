registros = []
sucessso = set()

while True:
    print("\nSelecione o status: ", "\n1 - Sucesso", "\n2 - Falha\n", "\nDigite 'parar' para sair/encerrar.\n", )
    entrada = input("Digite o nome de usuário: ")
    entrada = entrada.lower()

    if entrada == "parar":
        break
    

    while True:
        status = input("Opção: ")
        
        if status == "1":
            status = "sucesso"
            break
        elif status == "2":
            status = "falha"
            break
        else:
            print("Opção inválida, digite novamente!")

    while True:
        try:
            tempo = int(input("Digite o tempo em minutos: "))
            break
        except ValueError:
            print("Tempo inválido, digite novamente!")


    registros.append((entrada, status, tempo))
    if status == "sucesso":
        sucessso.add(entrada)
        print("\nAdicionado com sucesso!")

total_tempo = 0

for entrada, status, tempo in registros:
    if status == "sucesso":
        total_tempo += tempo

print(f"Registro de acessos: {registros}")

if sucessso:
    print(f"Acessos bem-sucedidos: {sucessso}")
else:
    print("Usuários com acesso bem-sucedido: Nenhum")
    
print(f"Tempo total das sessões bem-sucedidas: {total_tempo} minutos")