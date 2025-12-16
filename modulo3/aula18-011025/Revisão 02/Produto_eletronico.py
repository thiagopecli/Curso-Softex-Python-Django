"""Etapa 2: O Produto Eletrônico Especializado (no arquivo 
produto_eletronico.py) 
 
Um produto eletrônico é um produto, mas tem algumas características extras, 
como a garantia. 
Seu trabalho aqui: 
●  Crie uma classe chamada ProdutoEletronico que herda (pega emprestado) todas
as características da classe Produto. Isso é chamado de Herança. 
●  Adicione um atributo tempo_garantia_meses a esta classe. """

from Produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, quantidade_em_estoque, tempo_garantia_meses
                 ) -> None:
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tempo_garantia_meses = tempo_garantia_meses
    
    def get_tempo_garantia_meses(self):
        return self.tempo_garantia_meses
