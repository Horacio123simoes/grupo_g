class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def abrir_conta(self, cliente: dict, saldo_inicial: int):
        dono = cliente("horacio",'masculino',12/12/2002)
        dados = Conta('joao',20000,dono)
        self.contas.append(dados)

    def bloquear_conta(self, numero_conta: int):
        conta = self.buscar_conta(numero_conta)
        if conta:
            conta.bloqueada = True
            print(f"A conta número {numero_conta} foi bloqueada.")
        else:
            print(f"Conta número {numero_conta} não encontrada.")

    def transferir(self, numero_origem: int, numero_destino: int, valor: float):
        conta_origem = self.buscar_conta(numero_origem)
        conta_destino = self.buscar_conta(numero_destino)
        if not conta_origem:
            print(f"Conta número {numero_origem} não encontrada.")
            return
        if not conta_destino:
            print(f"Conta número {numero_destino} não encontrada.")
            return
        if conta_origem.bloqueada:
            print(f"A conta número {numero_origem} está bloqueada.")
            return
        if conta_destino.bloqueada:
            print(f"A conta número {numero_destino} está bloqueada.")
            return
        if conta_origem.saldo < valor:
            print("Saldo insuficiente.")
            return
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)
        print(f"Transferência de {valor:.2f} realizada com sucesso da conta {numero_origem} para a conta {numero_destino}")

    def fechar_conta(self, numero: int):
        for conta in self.contas:
            if conta.numero == numero:
                if conta.saldo > 0:
                    print("Esta conta possui saldo. Retire o valor antes de fechar.")
                    return
                if conta.bloqueada:
                    print("Esta conta está bloqueada. Desbloqueie antes de fechar.")
                    return
                self.contas.remove(conta)
                print(f"A conta número {numero} foi fechada.")
                return
        print(f"Conta número {numero} não encontrada.")

    def buscar_conta(self, numero_conta: int) -> object:
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        return None

