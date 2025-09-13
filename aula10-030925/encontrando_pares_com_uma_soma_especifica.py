"""10. Encontrando Pares com uma Soma Específica 

Dada uma lista de números e um valor alvo, encontre todos os pares de números na lista que 
somam o valor alvo. 
●  Entrada: Uma lista de números e um valor alvo (inteiro). 
●  Saída: Uma nova lista de listas, onde cada lista interna contém um par que soma o valor 
alvo."""

def encontrar_pares_com_soma(lista_numeros, valor_alvo):
    pares_encontrados = []
    tamanho_lista = len(lista_numeros)

    for i in range(tamanho_lista):
        for j in range(i + 1, tamanho_lista):
            if lista_numeros[i] + lista_numeros[j] == valor_alvo:
                par = [lista_numeros[i], lista_numeros[j]]
                pares_encontrados.append(par)
    return pares_encontrados

numeros = [2,7,3,11,8,1,15,6]
alvo = 9

print(f"Lista de entrada: {numeros}")
print(f"Valor alvo: {alvo}")

resultado = encontrar_pares_com_soma(numeros, alvo)
print(f"Pares encontrados: {resultado}")