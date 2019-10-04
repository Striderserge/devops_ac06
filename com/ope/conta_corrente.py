"""programa conta corrente"""

class Contacorrente:

    def __init__(self, numero, nomecorrentista, saldo=0.0):
        """recebe parametro"""
        self.numero = numero
        self.alterarnome(nomecorrentista)
        self.saldo = saldo

    def alterarnome(self, nomecorrentista):
        """altera o nome"""
        self.nomecorrentista = nomecorrentista

    def deposito(self, valor):
        """faz o deposito"""
        self.saldo += valor

    def saque(self, valor):
        """faz o saque"""
        self.saldo -= valor
