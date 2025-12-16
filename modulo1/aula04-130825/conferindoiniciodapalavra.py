# 2. Conferindo inicio da palavra:
# Peça uma palavra e verifique com .startswith() se ela começa com "py".
# Mostre "Essa palavra começa com 'py'!" ou "Essa palavra não começa com 'py'."

palavra = input("Digite uma palavra: ")

if palavra.startswith("py"):
    print(f"\nA palavra '{palavra}' começa com 'py'!")
else:
    print(f"\nA palavra '{palavra}' não começa com 'py'.")