# Contagem Reversa com range(): percorrer a lista de trás para frente.
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in range(len(numeros)-1, -1, -1):
    print(f"Este é o número {numeros[numero]} na contagem reversa")
