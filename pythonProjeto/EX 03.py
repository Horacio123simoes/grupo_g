class retangulo():
    def __init__(self,altura,largura):
        self.altura=altura
        self.largura=largura
    def calculo(self,altura,largura):
        self.area=self.altura*self.largura
        print("a area do retangulo e",self.area)
        self.perimetro=(2*altura)+(2*largura)
        print("o perimetro do retangulo e",self.perimetro)
retangulo1=retangulo(12,10)
retangulo1.calculo(12,14)