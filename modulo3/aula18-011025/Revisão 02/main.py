"""Etapa 4: Juntando Tudo (no arquivo main.py) 
 
Este é o arquivo principal, onde você vai "abrir a loja" e ver tudo funcionando. 
Seu trabalho aqui: 
●  Importe as classes Loja e ProdutoEletronico que você criou. 
●  Crie uma instância (um objeto) da sua Loja. 
●  Crie pelo menos dois objetos de produto, sendo um Produto genérico e outro um 
ProdutoEletronico. 
●  Use os métodos que você criou para: 
○  Adicionar os produtos ao estoque da sua Loja com quantidades diferentes. 
○  Usar o setter do produto para atualizar a quantidade em estoque, simulando 
uma venda. 
●  Chame o método verificar_estoque_de_produto() para mostrar que o estoque foi 
atualizado corretamente."""

# 1. Importa as classes necessárias dos outros arquivos
from Loja import Loja
from Produto import Produto
from Produto_eletronico import ProdutoEletronico

if __name__ == "__main__":
    minha_loja = Loja()
    print("--- Loja Aberta! ---")

    livro = Produto(nome="A Guerra dos Tronos", preco=75.50, quantidade_em_estoque=0)

    celular = ProdutoEletronico(nome="Smartphone XPTO", preco=3500.00, quantidade_em_estoque=0, tempo_garantia_meses=12)
    
    print("\n--- Abastecendo o Estoque ---")
    minha_loja.adicionar_produto_estoque(livro, 50)
    minha_loja.adicionar_produto_estoque(celular, 30)

    estoque_inicial_livro = minha_loja.verificar_estoque_de_produto("A Guerra dos Tronos")
    print(f"\nEstoque inicial de '{livro.nome}': {estoque_inicial_livro} unidades.")

    print("\n--- Simulando uma Venda ---")
    quantidade_vendida = 5
    
    if estoque_inicial_livro >= quantidade_vendida:
        print(f"Vendendo {quantidade_vendida} unidades de '{livro.nome}'...")
        
        novo_estoque = estoque_inicial_livro - quantidade_vendida
        
        livro.set_quantidade_em_estoque(novo_estoque)
        
        minha_loja.estoque[livro.nome] = novo_estoque
        
        print("Venda realizada e estoque atualizado!")
    else:
        print("Venda não pôde ser concluída. Estoque insuficiente.")

    estoque_final_livro = minha_loja.verificar_estoque_de_produto("A Guerra dos Tronos")
    print(f"\nEstoque final de '{livro.nome}': {estoque_final_livro} unidades.")