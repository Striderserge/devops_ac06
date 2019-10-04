"""testa a conta"""

from com.ope import conta_corrente

def teste1():
    """teste1"""
    conta = conta_corrente.Contacorrente(1234, "LucasPizza", 5)
    conta.alterarnome("LucasPiza")
    conta.deposito(1500)
    conta.saque(500)
