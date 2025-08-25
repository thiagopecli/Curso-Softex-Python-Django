# Verificar letra na palavra:
# Peça ao usuario uma palavra e depois uma letra. Informe se a letra esta na palavra:

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

if letra in palavra:
    print(f"A letra '{letra}' está na palavra.")
else: 
    print(f"A letra '{letra}' não está na palavra.")