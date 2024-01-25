import os


class conta():
    def __init__(self,nomecompleto,sexo,datadenascimento):
        self.nomecompleto=nomecompleto
        self.sexo=sexo
        self.datadenascimento=datadenascimento
        self.clientes = []
        self.contas = []

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

    def bloquear(self):
        print("conta bloqueada")

    def eliminar(self):
        print("conta eliminado com sucesso")


    def sair(self):
        os.system(exit(0))

    def menu(self):
        opcao = 0
        while opcao != 6:
            print("----------------------------------------")
            print("                HS BANK                 ")
            print("----------------------------------------")
            print("[1] Cadastrar Cliente")
            print("[2] Abertura de conta")
            print("[3] Bloquear Conta")
            print("[4] Eliminar Conta")
            print("[5] Mostra cliente")
            print("[6] Sair")
            print("----------------------------------------")
            opcao = int(input("digita a opcao: "))

            if opcao == 1:
                self.cadastrar()

            elif opcao == 2:
                self.Abertura()

            elif opcao == 3:
                self.bloquear()

            elif opcao == 4:
                self.eliminar()

            elif opcao == 5:
                self.mostra()

            elif opcao == 6:
                self.sair()

            else:
                print("Programa encerrada")
        print("Erro tente novamente!! escolha uma opção valida")

resultado=conta("horacio simoes","masculino",12/12/1999)
resultado.menu()






