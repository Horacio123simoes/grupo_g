class aluno():
    def __init__(self,nome,nota1,nota2):
        self.nome=nome
        self.nota1=nota1
        self.nota2=nota2
    def resolucao(self):
        nota1=int(input("digita a primeira nota: "))
        nota2=int(input("digita a segunda nota: "))
        #self.media=(self.nota1+self.nota2)/2
        self.media = (nota1+nota2)/2
        print("a media do",self.nome,"é:",self.media)
        if self.media>=10:
            print("o",self.nome,"está aprovado com sucesso")
        else:
            print("o",self.nome,"está reprovado com sucesso")
aluno1=aluno("Horácio",12,13)
aluno1.resolucao()