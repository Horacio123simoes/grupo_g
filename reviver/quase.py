
from  inicio import Banco
class Conta(Banco):
    numero = 1
    def __init__(self, cliente: dict, saldo_inicial: int):
        Banco.__init__(self)
        self.numero = Conta.numero
        Conta.numero += 1
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.bloqueada = False

    def sacar(self, valor: float):
        if not self.bloqueada:
            self.saldo -= valor
            print(f"Foi sacado {valor:.2f} da conta {self.numero}.")
        else:
            print(f"A conta {self.numero} está bloqueada.")

    def depositar(self, valor: float):
        if not self.bloqueada:
            self.saldo += valor
            print(f"Foi depositado {valor:.2f} na conta {self.numero}.")
        else:
            print(f"A conta {self.numero} está bloqueada.")

conta1=Conta('joao',20000)
conta1.sacar(1000)
conta1.depositar(30000)
