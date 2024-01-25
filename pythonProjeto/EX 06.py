class produtos():
    def __init__(self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade
    def compra(self,preco,quantidade):
        self.venda=preco*quantidade
        print("o total a pagar e",self.venda)
    def stoque(self,venda,quantidade):
        disponivel=self.venda-self.quantidade
        print("o valor total em stoque é:",disponivel)
        if self.quantidade>0:
            print("o produto está disponível")
        else:
            print("o produto não esta disponível")
produto1=produtos("arroz",20000,50)
produto1.compra(1000,2)
produto1.stoque(0,0)