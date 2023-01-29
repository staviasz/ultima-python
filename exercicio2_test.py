import pytest

from exercicio2 import add_item

def test_codigo_item():
    total = add_item(200)
    assert total == 5

def test_varios_codigo_itens():
    #Para esse teste ser mais fluido 
    #retire o cod de inserir mais pedidos 
    #deixando apenas o break
    lista = [100,101,105,200]
    valor_total = 0
    for i in iter(lista):
        valor_parcial = add_item(i)
        valor_total += valor_parcial
    assert valor_total == 42

