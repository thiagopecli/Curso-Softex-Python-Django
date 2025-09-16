# Jogo da Forca Simplificado
# ● Defina uma palavra secreta em uma variável (str).
# ● Use um while para dar ao usuário 5 chances de adivinhar a palavra.
# ● A cada tentativa, o usuário digita uma letra.
# ● Se a letra estiver na palavra, exiba as letras já descobertas (ex: _ y t _ _ n).
# ● Se a letra não estiver, diminua as chances.
# ● Se o usuário acertar todas as letras, imprima a palavra completa e uma mensagem de vitória. Se as chances acabarem, imprima a palavra e uma mensagem de derrota.

palavra_secreta = input("Digite a palavra secreta: ")
letras_descobertas = ["_"] * len(palavra_secreta)
chances = 5

while chances > 0:
    letra = input("Digite uma letra: ")

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_descobertas[i] = letra
        print("Letras descobertas:", " ".join(letras_descobertas))

        if "_" not in letras_descobertas:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break
    else:
        chances -= 1
        print("Letra incorreta. Você ainda tem", chances, "chances.")

if chances == 0:
    print("Você perdeu! A palavra era:", palavra_secreta)