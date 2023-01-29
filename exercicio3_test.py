import pytest

from exercicio3 import *

class TestFuncaoValidarMedida:

    def test_validar_medida_int_try(self):
        medida = validar_medida(2.5)
        assert medida == 2

    def test_validar_medida_int_exception(self):
        medida = validar_medida('2.5')
        assert medida == -1 

def test_calcular_multiplicador_peso():
    condicional_1 = calcular_multiplicador_peso(0)
    condicional_2 = calcular_multiplicador_peso(0.2)
    condicional_3 = calcular_multiplicador_peso(5)
    condicional_4 = calcular_multiplicador_peso(15)

    assert condicional_1 == 1
    assert condicional_2 == 1.5
    assert condicional_3 == 2
    assert condicional_4 == 3

class TestCauculadorDeRota:
    
    def test_calcular_multiplicador_rota_1(self):
        multiplicador = calcular_multiplicador_rota('sr')
        assert multiplicador == 1

    def test_calcular_multiplicador_rota_2(self):
        multiplicador = calcular_multiplicador_rota('sb')
        assert multiplicador == 1.2

    def test_calcular_multiplicador_rota_3(self):
        multiplicador = calcular_multiplicador_rota('br')
        assert multiplicador == 1.5

def test_ler_rota():
    lista = ['br', 'bs', 'rb', 'rs', 'sr', 'sb']
    rota = ler_rota()
    resposta = rota in lista
    assert resposta == True

def test_calcular_multiplicador_volume():
    condicional_1 = calcular_preco_volume(0)
    condicional_2 = calcular_preco_volume(1001)
    condicional_3 = calcular_preco_volume(10001)
    condicional_4 = calcular_preco_volume(30001)

    assert condicional_1 == 10
    assert condicional_2 == 20
    assert condicional_3 == 30
    assert condicional_4 == 20


def test_ler_peso_objeto_valido():
    peso = ler_peso_objeto()
    peso_aceito = peso < 30
    assert peso_aceito == True

def test_ler_dimensoes_objeto():
    volume = ler_dimensoes_objeto()
    assert volume == 27


def test_calcular_frete():
    total = calcular_frete(3,3,3)
    assert total == 27