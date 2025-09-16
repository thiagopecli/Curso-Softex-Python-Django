"""17. Combinador de Argumentos: Crie uma função que receba um argumento obrigatório 
(nome) e use *args e **kwargs para exibir todos os dados de forma clara. Imprima o resultado."""

def exibir_dados(nome: str, *args, **kwargs) -> None:
    print(f"Nome: {nome}")
    if args:
        print("Dados adicionais:")
        for dado in args:
            print(f" - {dado}")
    if kwargs:
        print("Detalhes:")
        for chave, valor in kwargs.items():
            print(f"  {chave}: {valor}")

exibir_dados("Produto A", "Embalagem: Caixa", "Peso: 1kg", preco=19.99, estoque=100)
exibir_dados("Usuário B", "Idade: 30", "Cidade: São Paulo", email="usuario@example.com")