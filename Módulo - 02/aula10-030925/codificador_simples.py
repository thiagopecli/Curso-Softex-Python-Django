"""9. Codificador Simples:

Crie um codificador simples. Para cada letra em uma lista de strings, mova-a uma posição para 
a frente no alfabeto (por exemplo, 'a' vira 'b', 'b' vira 'c'). 
●  Entrada: Uma lista de letras (strings de um único caractere). 
●  Saída: Uma nova lista com as letras codificadas."""

def codificador_simples(lista_de_letras):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    lista_codificada = []
    for letra in lista_de_letras:
        indice = alfabeto.find(letra)

        if indice == -1:
            lista_codificada.append(letra)
        else:
            novo_indice = (indice + 1) % len(alfabeto)

            nova_letra = alfabeto[novo_indice]
            nova_letra = alfabeto[novo_indice]
            lista_codificada.append(nova_letra)
    return lista_codificada

entrada = ['a', 'b', 'z', '!', 'T', ' ']
resultado = codificador_simples(entrada)

print(f"Lista original: {entrada}.")
print(f"Lista codificada: {resultado}")

entrada2 = ['p', 'y', 't', 'h', 'o', 'n']