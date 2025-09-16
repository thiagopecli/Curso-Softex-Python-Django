######## Operador in: A magia da Busca ########

# O operador "in" é uma ferramenta de busca, ela diz se existe ou não uma string em uma frase
frase = "Rafael viu que seus amigos Pedro, Ronaldo e Joaquina foram a sorveteria"
palavra_chave = "Ronaldo"

if palavra_chave in frase:
    print(f"Palavra {palavra_chave} encontrada!")
else: 
    print(f"Palavra {palavra_chave} não encontrada!")