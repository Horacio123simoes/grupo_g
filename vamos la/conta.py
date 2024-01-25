
import cliente
class conta(cliente):
    def __init__(self,numero,saldo_inicial,dono,limite):
        super().__init__(self,numero,saldo_inicial,limite)
        self.dono=dono
        self.contas=[]
        self.clientes=[]

    def consultarsaldo(self):
        print("Saldo disponivel:", self.saldo)

    def levantamento(self):
        self.valor = int(input('digita o valor a sacar: '))
        if (self.saldo < self.valor):
            return print('operacao invalida')
        else:
            self.saldo -= self.valor
            print("levantamento efectuado com sucesso!")

    def deposito(self, valor):
        self.saldo += valor
        print("Deposito efectuado com sucesso saldo actual é!", valor)

    def bloquear(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                conta.bloqueada = True
                return "Conta bloqueada com sucesso!"
        return "Conta não encontrada!"

    def fechar(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                self.contas.remove(conta)
                return "Conta fechada com sucesso!"
        return "Conta não encontrada!"

    def cadastrar(self):

        while True:
            print("---------------------------------------")
            print("              HS BANK                  ")
            print("---------------------------------------")
            print("           CADASTRAR CLIENTE           ")
            print("---------------------------------------")
            print("                                       ")
            print("Informe os dados do cliente")

            dadoscadastro = {}

            dadoscadastro["nomecompleto"] = (input("nome:"))
            dadoscadastro["sexo"] = (input("sexo:"))
            dadoscadastro["datadenascimento"] = (input("datadenascimento:"))

            dadoscadastro["numeroBI"] = input("numeroBI:")
            lista = {i["numeroBI"]: i for i in self.clientes}

            while dadoscadastro["numeroBI"] in lista:
                dadoscadastro["numeroBI"] = input("Bilhete em uso tente novamente")
            self.clientes.append(dadoscadastro)
            print("OK Cadastro concluido")
            opcao = input("Deseja cadastrar mais cliente? (S/N) ").strip().lower()
            if (opcao == "n"):
                self.menu()
                break

    def Abertura(self):

        while True:
            print("Indroduz o numero do bilhete do cliente")
            lista = {i["numeroBI"]: i for i in self.clientes}
            buscar = input("numeroBI")
            opcao = 0
            while opcao != 3:
                print("----------------------------------------")
                print("           ABERTURA DE CONTA            ")
                print("----------------------------------------")
                print("[1] Conta Poupança")
                print("[2] Conta Corrente")
                print("[3] Voltar")
                print("----------------------------------------")
                opcao = int(input("digita a opcao: "))

                if opcao == 1:

                    if buscar in lista:

                        print("Indroduz os dados para a abertura da conta")

                        dadosconta = {}
                        dadosconta["id"] = buscar
                        dadosconta["numerodaconta"] = input("numerodaconta:")
                        dadosconta["IBAN"] = input("IBAN:")
                        dadosconta["morada"] = input("morada:")
                        dadosconta["telefone"] = input("telefone:")
                        self.contas.append(dadosconta)
                        print('[ok! cadastro concluido]')
                        opcao = input("Deseja fazer abertura de outro cliente? (S/N) ").strip().lower()
                        if (opcao == "n"):
                            self.menu()
                            break
                    else:
                        print("Cliente não cadastrado!!, cadastre primeiro")
                        break
                        opcao = input("Deseja fazer abertura de outro cliente? (S/N) ").strip().lower()
                        if (opcao == "n"):
                            self.menu()
                            break

resultado = conta(12345,12000,'joao',5000)
resultado.cadastrar()
resultado.consultarsaldo()