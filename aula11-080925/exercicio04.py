"""4.  Crie um dicionário com os nomes de 3 países e suas capitais. Peça ao usuário para 
digitar o nome de um país e imprima a capital correspondente. Use dicionario.get() para 
evitar erros. """

paises = {
    "Brasil": "Brasilia",
    "França": "Paris",
    "Argentina": "Buenos Aires"
}

usuario = input("Digite o nome de um País: ")
pais_digitado = usuario.capitalize()
resultado = paises.get(pais_digitado, "Não encontrado.")

print(f"A Capital de {pais_digitado} é: {resultado}")