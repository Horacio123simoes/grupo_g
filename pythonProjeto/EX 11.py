class conta():
    def __init__(self,num,cliente):
        self.num=num
        self.cliente=cliente
    #def getnum(self):
        #return self.__num

    def setnum(self,num):
        self.__num=num




resultado=conta(12345,"Joao")
#print(resultado.getnum())
print(conta.setnum())
conta.setnum(3740)
print(conta.setnum)