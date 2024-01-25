import os


class banco():
    def __init__(self,dono,numero,saldo,limite):
        self.dono=dono
        self.numero=numero
        self.saldo=saldo
        self.limite=limite

    def menu(self):
        opcao = 0
        while opcao != 10:
            print('=========================BENVINDO AO BANK HKSV=========================')
            print('[1] Consultar saldo'
                  '\n[2] Levantamento'
                  '\n[3] Transferencia'
                  '\n[4] Deposito'
                  '\n[5] Cadastrar'
                  '\n[6] Abrir conta'
                  '\n[7] Bloquear conta'
                  '\n[8] Fechar conta'
                  '\n[9] Consulta cliente'
                  '\n[10] Sair')
            print('===============================================================')
            opcao = int(input("digita a opcao: "))
            if opcao == 1:
                self.consultarsaldo()

            elif opcao == 2:
                self.levantamento()

            elif opcao == 3:
                self.transferencia()
            elif opcao == 4:
                self.deposito()
            elif opcao== 5:
                self.cadastrar()
            elif opcao== 6:
                self.abertura()
            elif opcao== 7:
                self.bloquear()
            elif opcao== 8:
                self.fechar()
            elif opcao==9:
                self.consultar()
            elif opcao== 10:
                os.system(exit(0))
                break
            else:
                print('opcao invalida! tenta novamente')
                break

resultado = banco('horacio',123,20000,10000)
resultado.menu()


