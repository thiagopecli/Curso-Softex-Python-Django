# 3. Limpeza de entrada
# Peça ao usuario para digitar um texto com espaços no começo e no fim.
# Use .strip() para limpar e depois mostre o texto limpo. 

texto = input("Digite um texto contendo espaços: ")
texto_limpo = texto.strip()
print(f"\nTexto limpo(sem espaços): '{texto_limpo}'.")