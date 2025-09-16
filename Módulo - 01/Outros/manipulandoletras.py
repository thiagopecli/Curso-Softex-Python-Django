######## Metodo de manipulação de letras! ########

# Função .upper coloca o texto com CAIXA ALTA:
print("frase".upper())

# Função .lower() coloca o texto em caixa baixa:
print("FRASE".lower())

# Função .capitalize() coloca o texto com a primeira letra maiuscula, e a restante minuscula
print("FRASE".capitalize())

######## EXEMPLO ########

print("\n--- Sistema de Login ---")
nome1 = (input("Digite seu nome: "))
nome_maiuscula = nome1.upper()
nome2 = (input("Digite seu nome: "))
nome_minuscula = nome2.lower()
nome3 = (input("\nDigite seu nome: "))
nome_padrao = nome3.capitalize()

print(f"\nSeu nome Maiusculo: {nome_maiuscula}")
print(f"\nSeu nome Minusculo: {nome_minuscula}")
print(f"\nSeu nome Padrão: {nome_padrao}")