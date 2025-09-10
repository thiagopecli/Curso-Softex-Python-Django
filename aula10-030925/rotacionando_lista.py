# lista = [1,2,3,4,5]

# lista_final = lista[-2:]
# lista_inicio = lista[:-2]

# print(lista)
# print(lista_final + lista_inicio)

# Utilizando If e Else:

# lista1 = [1,2,3,4,5]
# posicao = 2

# if not lista1 or posicao == 0:
#     lista_rotacionada = lista1
# else:
#     rotacoes_reais = posicao % len(lista1)

#     if rotacoes_reais == 0:
#         lista_rotacionada = lista1

#     else:
#         parte_final = lista1[-rotacoes_reais:]
#         parte_inicial = lista1[:-rotacoes_reais]

#         lista_rotacionada = parte_final + parte_inicial

# print(f"Lista rotacionada: {lista_rotacionada}")

# Utilisando len()

lista_letras = ['a','b','c','d','e','f','g','h','i']
posicao_letras = 3
rotacoes_reais_letras = posicao_letras % len(lista_letras)
parte_final_letras = lista_letras[-rotacoes_reais_letras:]
parte_inicial_letras = lista_letras[:-rotacoes_reais_letras]
resultado_letras = parte_final_letras + parte_inicial_letras

print(resultado_letras)
