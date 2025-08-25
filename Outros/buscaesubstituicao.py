######## Métodos de Busca e Substituição! ########

# Função .replace(antigo) você substitui todas as ocorrencias de um pedaço do texto por outro.
frase = "Ronaldo brilha muito no Corinthians"
troca = frase.replace("Corinthians", "Brasil")
print(troca)

# Função .split() divide a sua string em várias partes e transforma o resultado em uma lista de strings
texto = "A qualidade do vencedor é nunca desistir e acreditar naquilo que ninguem acredita"
palavras = texto.split()
print(palavras)

# Função .join() faz o inverso do .split(), ele transforma as palvras em uma frase.
palavras_separadas = ['Olá ', 'pequeno ', 'DEV, ', 'seja ', 'bem ', 'recepcionado!']
frase = ''.join(palavras_separadas)
print(frase)