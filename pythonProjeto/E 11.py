class estacionamento():
    def __init__(self,lotacao):
        self.lotacao=lotacao
    def entra(self,entrada):
        if entrada<=self.lotacao:
            print("entrada de carro novo no parque de estacionamento",entrada)
        else:
            print("excesso de lotacao! nao e possivel adicionar um novo carro no estacionamento")
    def sai(self,saida):
        if saida<=self.lotacao:
            print("carro tirado com sucesso",saida)
        else:
            print("nao e possivel tirar esse carro! carro inexistente")
    def lugares(self,entrada,saida):
        if entrada<=self.lotacao:
            vagas=self.lotacao-entrada
            print("o numero de vagas desponivel apos a entrada e: ",vagas)
        if saida<=self.lotacao:
            vagas=vagas+saida
            print("o numero de vagas apos a saida e: ",vagas)
        else:
            print("opcao invalida")
resultado=estacionamento(40)
resultado.entra(10)
resultado.sai(4)
resultado.lugares(10,4)