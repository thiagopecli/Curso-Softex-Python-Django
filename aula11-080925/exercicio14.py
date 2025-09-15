"""14. Dada uma lista de palavras, crie um dicionário que conte a frequência de cada palavra."""

palavras = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("Frequência das palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")