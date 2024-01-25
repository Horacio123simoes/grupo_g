class ContaBancaria():
    def __init__(self,pini, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.pini=pini
    def autenticar(self):
        t=0
        while t<3:
            pini=int(input("inseri o pini: "))
            if self.pini==pini:
                return 1
            else:
                if t==2:
                    print("cartão bloqueado")
                    return 0
                else:
                    t+=1
    def consultarsaldo(self):
        if self.autenticar()==1:
            print("Saldo disponivel:",self.saldo)
    def levantamento(self,valor):
            self.saldo-=valor
            print("levantamento efectuado com sucesso!")
    def deposito(self,valor):
            self.saldo+=valor
            print("Deposito efectuado com sucesso saldo actual é!",valor)

    def extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.numero, self.saldo))

    #def transfere(self, destino, valor):
            #retirou = self.levantamento(valor)
            #if (retirou == False):
                #return False
            #else:
                #destino.deposita(valor)
                #return True
    def transfere(self, destino, valor):
        self.levantamento -= valor
        destino.saldo += valor

Conta1 = ContaBancaria(123,"Simoes",150122,100000)
Conta2 = ContaBancaria(123,"Horacio",166712,5000)


Conta1.consultarsaldo()

Conta2.consultarsaldo()
#Conta2.deposito(5000)
Conta1.deposito(200)
#Conta1.consultarsaldo()
conta1.transfere(1200,166712)
Conta1.levantamento(200)
Conta1.consultarsaldo()