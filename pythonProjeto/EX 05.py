class funcionarios():
    def __init__(self,nome,salario,cargo):
        self.nome=nome
        self.salario=salario
        self.cargo=cargo
    def subsideo(self,salario,sa,ss):
        self.bruto=sa+ss+salario
        print("salario bruto e",self.bruto,"kz")
    def imposto(self,inss,irt,ss):
        self.desconto=inss+irt+ss
        print("o total de desconto e",self.desconto,"kz")
        self.liquido= self.bruto-self.desconto
        print("salario liquido e",self.liquido,"kz")
funcionario1=funcionarios("horacio",12000,"enginheiro")
funcionario1.subsideo(12000,5000,3000)
funcionario1.imposto(0.03,0.06,0.03)

