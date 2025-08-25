#  5.TuplaseConjuntos: 

#  Dada a tupla cores = ("vermelho","verde", "azul","verde"):
#       Converta-a em um conjunto para remover duplicatas
#       Adicione a cor "amarelo" ao conjunto

cores = ("vermelho", "verde", "azul", "verde")
conjunto_cores = set(cores) # Conjunto sem duplicatas.
conjunto_cores.add("amarelo") # Adicionando a cor amarelo.

print(conjunto_cores)