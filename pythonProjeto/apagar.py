class animal():
    def __init__(self,nome) -> None:
        self.nome = nome
    def comer(self):
        print("Comer")
    def locomover(self):
        print("Locomovendo,animal")

class mamifero(animal):
    def __init__(self, nome,pelo) -> None:
        super().__init__(nome)
        self.pelo = pelo
    def locomover(self):
        print("Mamifero,locomovendo")
    def amamentar(self):
        print("Amamentar")
        print(self.nome)

class ave(animal):
    def __init__(self, nome,pena) -> None:
        super().__init__(nome)
        self.pena = pena
    def ovar(self):
        print("Já ovou")
        print(self.nome,self.pena)

class pessoa(mamifero):
    def __init__(self, nome, cabelo) -> None:
        super().__init__(nome, cabelo)
        self.cabelo = cabelo
    def falar(self):
        print("Pessoa,Falando")

user = animal("Anticristo")
user.comer()
user.locomover()
user = mamifero("Anticristo","Pelo")
user.amamentar()
user = ave("Galinha","Pena")
user.ovar()
user = pessoa("Anticristo","Castanho")
user.locomover()