class Banco():
    def __init__(self):
        self.clientes = []
        self.contas = []

    def cadastrar_cliente(self, nome, sexo, data_nascimento):
        cliente = Cliente(nome, sexo, data_nascimento)
        self.clientes.append(cliente)
        print("Cliente cadastrado com sucesso.")

    def abrir_conta(self, numero, saldo_inicial, cliente, tipo_conta):
        if tipo_conta == "Salário":
            conta = ContaSalario(numero, saldo_inicial, cliente)
        elif tipo_conta == "Poupança":
            conta = ContaPoupanca(numero, saldo_inicial, cliente)
        else:
            return "Tipo de conta inválido!"
        self.contas.append(conta)

    def fechar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                return "Conta fechada com sucesso!"
        return "Conta não encontrada!"

    def bloquear_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                conta.bloqueada = True
                return "Conta bloqueada com sucesso!"
        return "Conta não encontrada!"


class Cliente():
    def __init__(self, nome, sexo, data_nascimento):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento


class ContaSalario():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.bloqueada = False


class ContaPoupanca():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.bloqueada = False

