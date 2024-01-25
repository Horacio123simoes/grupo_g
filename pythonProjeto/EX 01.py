class circulo():
    def __init__(self,raio):
        self.raio=raio
    def calculo(self,raio):
        pi=3.14
        area=pi*raio**2
        print("a area do circulo e",area)
        perimetro=2*pi*raio
        print("o perimetro do circulo e",perimetro)
circulo1=circulo(0)
circulo1.calculo(10)