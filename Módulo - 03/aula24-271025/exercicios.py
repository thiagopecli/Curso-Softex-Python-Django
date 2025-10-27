import random

# Exercício 2

def rotacionar_lista(lista: list, k: int) -> list:
    if not lista:
        return []
    
    tamanho = len(lista)
    k = k % tamanho
    
    parte_final = lista[-k:]
    parte_inicial = lista[:-k]
    
    return parte_final + parte_inicial

# Exercício 11

def contar_palavras_com_excecao(texto: str) -> dict:

    contagem = {}
    palavras = texto.lower().split() 
    
    for palavra in palavras:
        palavra_limpa = palavra.strip('.,!?;:"()[]{}')
        if not palavra_limpa:
            continue
            
        try:
            contagem[palavra_limpa] += 1
        except KeyError:
            contagem[palavra_limpa] = 1
            
    return contagem

# Exercício 21

class ItemInventario:
    def __init__(self, nome: str, quantidade: int, valor_unitario: float):
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        if valor_unitario < 0:
             raise ValueError("Valor unitário não pode ser negativo.")
             
        self.nome = nome
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

    def valor_total(self) -> float:
        return self.quantidade * self.valor_unitario
