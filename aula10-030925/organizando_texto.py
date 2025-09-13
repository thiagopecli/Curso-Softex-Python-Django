lista_de_palavras = ["\nO", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma."]
texto_final = ""

for palavra in lista_de_palavras:
    texto_final += palavra + "\n"

print(f"Texto utilizando for: {texto_final}")

# Utilizando o metodo ".join()"

lista_de_palavras2 = ["\nO", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma."]
texto_final2 = "\n".join(lista_de_palavras2)
print(f"Texto utilizando .Join(): {texto_final2}")