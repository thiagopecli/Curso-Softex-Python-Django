"""16. Detalhes do Produto: Crie uma função que receba o nome de um produto e use 
**kwargs para exibir detalhes adicionais como preço, marca e estoque. Imprima o resultado."""

def exibir_detalhes_produto(nome: str, **kwargs) -> None:
    print(f"Detalhes do produto '{nome}':")
    for chave, valor in kwargs.items():
        print(f"  {chave}: {valor}")

exibir_detalhes_produto("Smartphone", preco=1999.99, marca="Marca X", estoque=50)