import pytest

from exercicio4 import *


def test_gerando_cod_lista_vazia():
    codigo = gerar_codigo()
    assert codigo == 1

def test_gerando_cod_lista_com_dados():
    '''codigo testado apos o primeiro append'''
    codigo = gerar_codigo()
    assert codigo == 2
    
def test_adicao_de_pecas():
    pecas = [cadastrar_peca()]
    resultado = pecas[0]
    assert resultado == [{'codigo': 1,
                        'nome': 'celular',
                        'fabricante': 'motorola',
                        'valor': 2200}]
