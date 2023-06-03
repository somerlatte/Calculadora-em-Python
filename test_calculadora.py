import pytest
from calculadora import Calculadora


def test_adicao():
    calculadora = Calculadora()
    resultado = calculadora.adicao(2, 3)
    assert resultado == 5

def test_subtracao():
    calculadora = Calculadora()
    resultado = calculadora.subtracao(5, 3)
    assert resultado == 2

def test_multiplicacao():
    calculadora = Calculadora()
    resultado = calculadora.multiplicacao(2, 3)
    assert resultado == 6

def test_divisao():
    calculadora = Calculadora()
    resultado = calculadora.divisao(6, 3)
    assert resultado == 2

def test_divisao_por_zero():
    calculadora = Calculadora()
    resultado = calculadora.divisao(6, 0)
    assert resultado == "Erro: não é possível dividir por zero"
