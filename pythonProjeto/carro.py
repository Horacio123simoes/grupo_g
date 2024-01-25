class carro():
    def __init__(self,marca,modelo,velocidade_actual):
        self.marca=marca
        self.modelo=modelo
        self.velocidade_actual=velocidade_actual
    def velocidade(self):
        print('a velocidade actual do carro é',self.velocidade_actual,'km/h')

    def acelera(self,valor):
        self.velocidade_actual+= valor
        print('a acileração do carro é de:',valor,'km/h')
    def frear(self,valor):
        self.velocidade_actual-= valor
        print('o carro freou a',valor,'km/h')

resultado= carro('BMW','we32',150)
resultado.velocidade()
resultado.acelera(120)
resultado.velocidade()
resultado.frear(50)
resultado.velocidade()
