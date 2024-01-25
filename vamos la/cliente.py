import banco
class cliente(banco):
    def __init__(self,nome,sexo,data_nasc):
        super().__init__(self,nome)
        self.sexo=sexo
        self.data_nasc=data_nasc


