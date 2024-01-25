class Banco():
    def __init__(self) -> None:
        pass
    def abrir_conta(self,nome,saldo,n_telefone,n_bilhete,morada):
        self.nome = nome
        self.saldo = saldo
        import random
        n_conta = random.randint(10000,1000000)
        pin = random.randint(0,1000)
        self.n_telefone = n_telefone
        self.n_bilhete = n_bilhete
        self.morada = morada
        print(f"""              
              Conta Aberta:
              Seja Bem-Vindo/a {self.nome}
              
                 *Informações*
                
                  Nome: {self.nome}
                  N Conta: {n_conta}
                  Pin: {pin}
                  Saldo: {self.saldo} Kz
                  N Telefone: {self.n_telefone}
                  N Bilhete: {self.n_bilhete}
                  Morada: {self.morada}
              """)
    def fechar_conta(self,n_conta,pin):
        if n_conta == n_conta and pin == pin:
            print(f"""         
                                *Fechar Conta*
                                  Olá {self.nome}
                                  Conta Bancária Fechada!
                  """)
        elif n_conta != n_conta:
            print("Número de Conta Inválido")
        elif pin != pin:
            print("Pin Inválido")
        else:
            print("Inválido")
            
    def bloquear_conta(self,n_conta,pin):
        if n_conta == n_conta and pin == pin:
            print(f"""          
                                    *Bloquear Conta*
                                      Olá {self.nome}
                                      Conta Bancária Bloqueada!
                  """)
        elif n_conta != n_conta:
            print("Número de Conta Inválido")
        elif pin != pin:
            print("Pin Inválido")
        else:
            print("Inválido")
    
    def saques(self,pin,sacar):
        self.sacar = sacar
        saldo_liquido = self.saldo - self.sacar
        if pin == pin and self.saldo >= self.sacar:
            self.saques  = self.saldo - self.sacar
            print(f"""
                                      *Área de Levantamento*
                                      
                                  Retirado: {self.sacar} Kz
                                  Saldo Liquído: {saldo_liquido} Kz
                   """)
        elif pin != pin:
             print("Pin Inválido!")
        elif self.saldo < self.sacar:
             print("Saldo Insuficiente!")
        else:
            print("Inválido!")
            
    def deposito(self,pin,depositar):
        self.depositar = depositar
        saldo_liquido = self.saldo - self.depositar
        if pin == pin and self.saldo >= self.depositar:
            self.deposito = self.saldo - self.depositar
            print(f"""
                            *Área de Deposito*
                            Depositou: {self.depositar} Kz
                            Saldo Liquído: {saldo_liquido} Kz
                  """)
        elif pin!= pin:
            print("Pin Inválido!")
        elif self.saldo < self.depositar:
            print("Saldo Insuficiente!")
        else:
            print("Inválido!")
            
    def transferencias(self,nome,pin,numero_conta,transferir):
        self.nome = nome
        self.numero_conta = numero_conta
        self.transferir = transferir
        saldo_liquido = self.saldo - self.transferir
        if pin == pin and self.saldo >= self.transferir:
            print(f"""
                            *Área de Transfêrencias*
                            
                             Transferência para {self.nome}
                             Número de Conta: {self.numero_conta}
                             Valor Transferido: {self.transferir} kz
                             Saldo Liquído: {saldo_liquido}
                  """)
        elif pin != pin:
            print("Pin Inválido!")
        elif self.saldo < self.transferir:
            print("Saldo Inválido!")
        else:
            print("Inválido!")
    def consultas(self,pin,n_conta):
        self.consultas = self.saldo
        if pin == pin:
            print(f"""
                              *Área de Consultas*
                              
                              Proprietario: {self.nome}
                              N De Conta: {n_conta}
                              Saldo Liquído: {self.saldo}
                  """)
        else:
            print("Inválido!")    
        
    
user1 = Banco()
user1.abrir_conta("Sálvio",1000,931212105,1234456,"Cacuaco")
user1.fechar_conta(12928,470)
user1.bloquear_conta(28814,577)
user1.saques(455,300)
user1.deposito(566,300)
user1.transferencias("Helena",566,2345566,300)
user1.consultas(455,2345566)
