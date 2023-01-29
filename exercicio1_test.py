import pytest
from exercicio1 import descontos

def test_desconto_entre_10_e_99_unidades():
    desconto = descontos(10)
    assert desconto == 0.95


def test_desconto_entre_100_e_999_unidades():
    desconto = descontos(999)
    assert desconto == 0.90

def test_desconto_acima_de_1000():
    desconto = descontos(1000)
    assert desconto == 0.85

def test_menor_de_10():
    desconto = descontos(9)
    assert desconto == 1