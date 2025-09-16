"""18. União de Dicionários: Crie dois dicionários. Crie um terceiro dicionário que seja a união 
dos dois primeiros. Se uma chave existir em ambos, use o valor do segundo dicionário. """

dicionario1 = {'a': 1, 'b': 2}
dicionario2 = {'b': 3, 'c': 4}
dicionario_uniao = dicionario1.copy()
dicionario_uniao.update(dicionario2)
print(dicionario_uniao)
