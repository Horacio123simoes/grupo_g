import os


class ContaBancaria():
    def __init__(self,pini, nome, numero, saldo):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.pini=pini
        self.clientes = []
    def autenticar(self):
        t=0
        while t<3:
            pini=int(input("inseri o pini: "))
            if self.pini==pini:
                return 1
            else:
                if t==2:
                    print("acesso negado")
                    return 0
                else:
                    t+=1

    def menu_principal(self):

        opcao = 0
        while opcao != 3:
            print('==================BENVINDO AO BANCO SIMOES=====================')
            print('========================MENU PRINCIPAL========================')
            print('[1] ATM'
                    '\n[2] Balcao'
                    '\n[3] sair')
            print('===============================================================')
            opcao = int(input("digita a opcao: "))
            if opcao == 1:
                self.atm()

            elif opcao == 2:
                self.balcao()

            elif opcao==3:
                self.sair()

            else:
                print('opcao invalida! tenta novamente')
        print('fim do programa tenta acertar')
        os.system(exit(0))

    def atm(self):
        if self.autenticar() == 1:
            opcao = 0
            while opcao != 4:
                print('=========================SERVICOS ATM=========================')
                print('[1] Consultar saldo'
                  '\n[2] levantamento'
                  '\n[3] transferencia'
                  '\n[4] Voltar')
                print('===============================================================')
                opcao = int(input("digita a opcao: "))
                if opcao == 1:
                    self.consultarsaldo()

                elif opcao == 2:
                    self.levantamento()

                elif opcao == 3:
                    self.transferencia()
                elif opcao==3:
                    self.menu_principal()
                    break


                else:
                    print('opcao invalida! tenta novamente')
            print('fim do programa tenta acertar')

    def consultarsaldo(self):
        print('===============CONSULTA DO SALDO==================')
        print("Saldo disponivel:", self.saldo)
        print('==================================================')
    def levantamento(self):
        self.valor=int(input('digita o valor a sacar: '))
        self.saldo -= self.valor
        print('===============LEVANTAMENTO==================')
        print("levantamento efectuado com sucesso!")
        print('=============================================')
    def extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.numero, self.saldo))

    #def transferencia(self, destino, valor):
        #retirou = self.levantamento(valor)
        #if (retirou == False):
            #return False
        #else:
            #destino.deposita(valor)
            #return True
    #def transferencia(self, destino, valor):
        #self.levantamento -= valor
        #destino.saldo += valor

    def balcao(self):
        opcao = 0
        while opcao != 11:
            print('=========================ATENDIMENTO AO BALCAO=========================')
            print('[1] Consultar cliente'
                  '\n[2] levantamento'
                  '\n[3] Transferencia'
                  '\n[4] Deposito'
                  '\n[5] Abertura de conta'
                  '\n[6] Fechar conta'
                  '\n[7] Bloquear conta'
                  '\n[8] Cadastra cliente'
                  '\n[9] Consultar cadastro'
                  '\n[10]Consulta conta'
                  '\n [11] Volta')
            print('========================================================================')
            opcao = int(input("digita a opcao: "))
            if opcao == 1:
                self.consultarcliente()
            elif opcao == 2:
                self.levantamento()
            elif opcao == 3:
                self.transferencia()
            elif opcao== 4:
                self.deposito()
            elif opcao== 5:
                self.abertura()
            elif opcao == 6:
                self.fechar()
            elif opcao== 7:
                self.bloquear()
            elif opcao==8:
                self.cadastro()
            elif opcao==9:
                self.consulta_cliente()
            elif opcao==10:
                self.consulta_conta()
            elif opcao==11:
                self.menu_principal()
                break
            else:
                print('opcao invalida! tenta novamente')
        print('fim do programa tenta acertar')

    def cadastro(self):
        while True:
            print('insere os dados do cliente')
            dados = {}
            dados['nome_completo'] = input('insere o nome completo: ')
            dados['sexo'] = input('insere o sexo: ')
            dados['data_nasc'] = input('insere a data de nascimento: ')

            dados['email'] = input('insere o email: ')
            lista = {i['email']: i for i in self.clientes}
            while dados['email'] in lista:
                dados['email'] = input('[email em uso,tenta novamente!]email')

            dados['telefone'] = int(input('insere o telefone: '))
            lista = {i['telefone']: i for i in self.clientes}
            while dados['telefone'] in lista:
                dados['telefone'] = input('[telefone em uso,tenta novamente!]telefone:')

            self.clientes.append(dados)

            print('[ok! cadastro concluido]')
            opcao = input('deseja cadastra mais alguem? (S/N): ').strip().lower()
            if (opcao == 'n'):
                self.balcao()
                break

    def consultar_cliente(self,clientes,nome_completo,email):
        while True:
            print('')
            print('[usuarios cadastrado!]')
            print('')
            for i in clientes:
                print('nome: ', i[nome_completo], i[email])
            print('')
            opcao = input('deseja conferir novamente : (S/N)').strip().lower()
            if opcao == 'n':
                self.balcao()
                break

    def sair(self):
        os.system(exit(0))

resultado1 = ContaBancaria(123, "Simoes", 150122, 10000)
resultado2 = ContaBancaria(1234, "Horacio", 166712,15000)


resultado2.menu_principal()
resultado2.atm()
resultado2.balcao()
resultado2.consultarsaldo()
resultado2.levantamento()
resultado2.consultarsaldo()
resultado2.cadastro()
resultado2.consultar_cliente()
#resultado2.transferencia(resultado1,200)
