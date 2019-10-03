def valorpagamento(valor, diasatraso):
    """verifica o valor a ser pago de uma prestação"""

    if valor < 0:
        '''verifica se o valor é zero'''
        return None
    if diasatraso > 0:
        '''verifica se o valor de atraso é maior que 0'''
        multa = valor * 0.03
        adicionalatraso = valor * (diasatraso * 0.01)
        return valor + multa + adicionalatraso
    return valor
