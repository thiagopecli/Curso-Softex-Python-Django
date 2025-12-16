lista = [[15,40,60], [25,35,45], [105,125,225]]
nova_lista = []

for sublista in lista:
    if not sublista:
        media = 0
    else:
        soma_itens = sum(sublista)
        quantidade_itens = len(sublista)
        media = soma_itens / quantidade_itens
    nova_lista.append(round(media, 2))

print(nova_lista)