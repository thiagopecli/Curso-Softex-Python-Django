"""13. Verificando um Subconjunto: 
Crie dois conjuntos: pratos_veganos = {'salada', 'arroz', 
'feijão'} e cardapio = {'pizza', 'salada', 'arroz', 'feijão'}. Verifique se pratos_veganos é um 
subconjunto de cardapio."""

pratos_veganos = {'salada', 'arroz', 'feijão'}
cardapio = {'pizza', 'arroz', 'feijão', 'carne'}
print(f"Esses são os pratos veganos: {pratos_veganos}")
print(f"Esses são os pratos do cardapio: {cardapio}")

resultado_check = pratos_veganos.issubset(cardapio)
if resultado_check:
    print("Sim, 'pratos veganos' é um subconjunto de 'cardapio'.")
else:
    print("Não, 'pratos veganos' não são um subconjunto de 'cardapio'")