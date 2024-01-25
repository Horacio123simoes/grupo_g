class paciente():
    def __init__(self,nome,idade,historico):
        self.nome=nome
        self.idade=idade
        self.historico=historico
    def consulta(self,novo):
        self.historico=["alergico a lactose"]
        #for i in range (len(self.historico)):
       # while len(self.historico):#
        self.historico.append(novo)
        print(self.historico)
            #self.historico=self.historico+1#
paciente1=paciente("joao",19,"alergico a lactose")
paciente1.consulta("diarreia,diabete")