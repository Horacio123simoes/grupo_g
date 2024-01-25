class cartao:
    def __init__(self, nome, pin, saldo):
        self.nome = nome
        self.pin = pin
        self.saldo = saldo
    def consultar(self):
        print("o saldo actual e ", self.saldo)
    def saque(self):
        valor=float(input("Digite o valor a sacar"))
        valor - self.saldo
        if valor>self.saldo:
            print("Operação invalida")
        else:
            print("Saque de", valor, "efectuado com sucesso")
    def autenticar (self):
     for tentativas in range(0,3):
        pin = int(input("insira o pin: "))
        pin == 1230
        if pin == 1230:
            print("acesso livre")
            self.consultar()
            self.saque()
            break
        else:
            print("acesso negado")
        if tentativas in range(2,0,-2):
            print("cartao bloqueado")
            break
cart=cartao("Diboba", 1230, 100000)
cart.autenticar()
