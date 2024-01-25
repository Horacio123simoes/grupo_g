import os


class cantina():
    def __init__(self,nome,senha):
        self.nome=nome
        self.senha=senha
        self.nome=['feijao','arroz','massa']
        self.preco=[500,600,350]
        self.quantidade=[50,80,30]
    def autenticar(self):
        t = 0
        while t < 3:
            senha = int(input("insere a senha: "))
            if self.senha == senha:
                return 1
            else:
                if t == 2:
                    print("senha errado")
                    return 0
                else:
                    t += 1

    def espere(self,wait):
        print("precione 1 para sair do programa\n")
        print("precione qualquer número para voltar\n")
        if (wait==1):
            os.system(exit(0))
        else:
            print("")
            self.menu()
            os.system(exit(0))


    def mostra_produto(self):
        print('=========CONSULTA==========')
        print('nome do produto:',self.nome[0])
        print('preco do produto:',self.preco[0])
        print('quantidade do produto:',self.quantidade[0])
        print('===========================')
        os.system('cls')
        #self.nome.append('frango')
        #self.preco.append(600)
        #self.quantidade.append(45)
        #print(self.nome)
        #print(self.preco)
        #print(self.quantidade)

    def vender_produto(self):
        #print('digita o nome do produto q deseja compra?',self.nome[1])
        #print('digita o preco do produto q deseja compra?',self.preco[1])
        #print('digita a quantidade do produto q deseja compra?',self.quantidade[1])
        #self.compra=self.preco[1]*self.quantidade[1]
        self.nome=input('digita o nome do produto q deseja compra?: ')
        #self.preco=int(input('digita o preco do produto q deseja compra?: '))
        self.quantidade=int(input('digita a quantidade do produto q deseja compra?: '))
        self.quantidade-=self.quantidade
        print('venda feito com sucesso',self.quantidade)


    def sair(self):
        os.system(exit(0))

    def menu(self):
        if self.autenticar() == 1:
            opcao=0
            while opcao !=3:
                print('===============BENVINDO A CANTINA VAI A MERDA==================')
                print('==============================MENU=============================')
                print('[1] Mostrar produto'
                      '\n[2] Vender produtos'
                      '\n[3] sair')
                print('===============================================================')
                opcao=int(input("digita a opcao: "))
                if opcao==1:
                    self.mostra_produto()
                elif opcao==2:
                    self.vender_produto()
                elif opcao==3:
                    self.sair()
                else:
                    print('opcao invalida! tenta novamente')
            print('fim do programa tenta acertar')

resultado=cantina("vai a merda",1234)

resultado.menu()

resultado.mostra_produto()

resultado.vender_produto()

resultado.sair()