"""Escreva um programa que pede ao usuário para digitar uma frase e conta quantas palavras 
ela tem. Use um loop for para percorrer a string. """

frase_digitada = input("Digite uma frase: ")
contador_palavras = 0 # INICIALIZAR AS VARIÁVEIS
espaço = True # Começamos "fora de uma palavra" (ou em um espaço)

for palavra in frase_digitada: # PERCORRER CADA CARACTERE DA FRASE

    if not palavra.isspace(): # A LÓGICA DE DECISÃO: Se o caractere atual NÃO é um espaço, .isspace() é melhor que ' ' pois pega tabs, etc.
        if espaço: # E nós estávamos anteriormente em um espaço...
            contador_palavras += 1 # ...então encontramos o início de uma nova palavra!
            espaço = False # Agora, mudamos nosso estado para "dentro de uma palavra"
    else: # Se o caractere atual É um espaço
        espaço = True # Mudamos nosso estado para "fora de uma palavra"

print(f"Esta frase contém {contador_palavras} palavras")