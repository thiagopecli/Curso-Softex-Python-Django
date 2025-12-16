"""10. Crie um dicionário com cores e seus códigos hexadecimais. Use um loop while para 
permitir que o usuário procure o código de uma cor repetidamente. O loop deve terminar 
quando o usuário digitar "sair"."""

cores = {
    "vermelho": "#FF0000",
    "verde": "#00FF00",
    "azul": "#0000FF",
    "preto": "#000000",
    "branco": "#FFFFFF"
}

while True:
    cor = input("Digite o nome da cor (ou 'sair' para encerrar): ")
    if cor == "sair":
        break
    elif cor in cores:
        print(f"Código hexadecimal de {cor}: {cores[cor]}")
    else:
        print("Cor não encontrada.")