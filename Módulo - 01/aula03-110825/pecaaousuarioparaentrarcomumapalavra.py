# Peça ap usuario para entrar com uma palavra
# Ela tem que começar com "p"
# Ela tem que terminar com "s"
# A palavra deve conter a letra "i" em qualquer posição
# a palavra não deve ter "m" nem "n"
# ela deve ter no minimo 3 caracteres
# a palavra deve ser toda em minusculas
# o programa deve execuutar até que as condiçoes sejam atendidas


while True:
    palavra = input("Digite uma palavra: ").lower()
    if len(palavra) < 3:
        print("A palavra deve ter no mínimo 3 caracteres.")
    elif palavra[0] != "P":
        print("A palavra deve começar com 'P'.")
    elif palavra[len(palavra) -1] != "S":
        print("A palavra deve terminar com 'S'.")
    elif "I" not in palavra:
        print("A palavra deve conter a letra 'I'.")
    elif "M" in palavra or "N" in palavra:
        print("A palavra não deve conter 'M' nem 'N'.")
    else:
        print("Palavra aceita!")
        break
