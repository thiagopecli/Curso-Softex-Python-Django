import pytest
from exercicios import rotacionar_lista, contar_palavras_com_excecao, ItemInventario

# Exercício 2

def test_rotacionar_lista_simples():
    assert rotacionar_lista([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotacionar_lista_zero_posicoes():
    assert rotacionar_lista([1, 2, 3], 0) == [1, 2, 3]

def test_rotacionar_lista_mais_que_tamanho():
    assert rotacionar_lista(['a', 'b', 'c'], 4) == ['c', 'a', 'b'] 

def test_rotacionar_lista_tamanho_igual_rotacao():
     assert rotacionar_lista([10, 20], 2) == [10, 20] 

def test_rotacionar_lista_vazia():
    assert rotacionar_lista([], 3) == []

# Exercício 11

def test_contagem_palavras_simples():
    texto = "isso é um teste isso é"
    esperado = {"isso": 2, "é": 2, "um": 1, "teste": 1}
    assert contar_palavras_com_excecao(texto) == esperado

def test_contagem_palavras_com_pontuacao_e_maiusculas():
    texto = "Olá, Mundo! Olá Python."
    esperado = {"olá": 2, "mundo": 1, "python": 1}
    assert contar_palavras_com_excecao(texto) == esperado

def test_contagem_palavras_vazio():
    assert contar_palavras_com_excecao("") == {}

def test_contagem_palavras_apenas_espacos_ou_pontuacao():
     assert contar_palavras_com_excecao("  , ! ? ") == {}

# Exercício 21

def test_item_inventario_criacao_e_valor_total():
    item = ItemInventario(nome="Caneta", quantidade=100, valor_unitario=1.50)
    assert item.nome == "Caneta"
    assert item.quantidade == 100
    assert item.valor_unitario == 1.50
    assert item.valor_total() == 150.00

def test_item_inventario_valor_total_zero_quantidade():
    item = ItemInventario(nome="Borracha", quantidade=0, valor_unitario=2.00)
    assert item.valor_total() == 0.00

def test_item_inventario_valor_total_zero_preco():
     item = ItemInventario(nome="Lápis", quantidade=50, valor_unitario=0.00)
     assert item.valor_total() == 0.00

def test_item_inventario_quantidade_negativa_levanta_erro():
    with pytest.raises(ValueError, match="Quantidade não pode ser negativa."):
        ItemInventario(nome="Régua", quantidade=-10, valor_unitario=3.00)

def test_item_inventario_valor_negativo_levanta_erro():
    with pytest.raises(ValueError, match="Valor unitário não pode ser negativo."):
        ItemInventario(nome="Apontador", quantidade=20, valor_unitario=-1.00)
