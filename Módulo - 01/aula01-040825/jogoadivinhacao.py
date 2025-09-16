# Jogo de Adivinhação com Dicas 
# ● Defina um número secreto. 
# ● Use um while True e um contador de tentativas. 
# ● A cada tentativa, diga se o palpite é "maior" ou "menor" que o número secreto. 
# ● Quando o usuário acertar, imprima a mensagem de vitória e quantas tentativas foram 
# necessárias.

numero_secreto = 42
tentativas = 0

print("=== Jogo de Adivinhação ===")
print("Tente adivinhar o número secreto entre 1 e 100!")
while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Tente um número maior!")
    elif palpite > numero_secreto:
        print("Tente um número menor!")
    else:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
        break
    