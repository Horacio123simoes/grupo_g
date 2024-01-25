from pythonProjeto.trabalho import Conta


class Cliente():
    def __init__(self, nome, sexo, data_nasc):
        super().__init__(nome)
        self.sexo = sexo
        self.data_nasc = data_nasc





cliente	= Cliente('João',	'masculino',	'03/05/2000')
minha_conta	= Conta('123-4',	cliente,	120.0,	1000.0)