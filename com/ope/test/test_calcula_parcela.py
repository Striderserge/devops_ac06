import pytest
from com.ope.calcula_parcela import valorpagamento

def test_calcula_parcela1():
    assert valorpagamento(10, 5) == 10.8, "Deverá ser 10.8"

def test_calcula_parcela2():
    assert valorpagamento(-5, 0) == None, "Deverá ser None"

def test_calcula_parcela3():
    assert valorpagamento(10, 0) == 10, "Deverá ser 10"
