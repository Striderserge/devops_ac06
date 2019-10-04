"""teste do calcula calcula parcela"""

from com.ope.calcula_parcela import valorpagamento

def test_calcula_parcela1():
    """teste 1"""
    assert valorpagamento(10, 5) == 10.8, "Deverá ser 10.8"

def test_calcula_parcela2():
    """teste 2"""
    assert valorpagamento(-5, 0) is None, "Deverá ser None"

def test_calcula_parcela3():
    """teste 3"""
    assert valorpagamento(10, 0) == 10, "Deverá ser 10"
