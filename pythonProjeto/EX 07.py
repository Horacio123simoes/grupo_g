class triangulo():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calculo(self,lado1,lado2,lado3):
        if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
            print("o triangulo e valido")
            area=self.base*self.altura/2
            print("area e",area)
        else:
            print("o triangulo nao e valido")
triangulo1=triangulo(15,10)
triangulo1.calculo(7,10,4)