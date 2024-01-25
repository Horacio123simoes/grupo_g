class alunos():
    def __init__(self,nome,nota1,nota2,matricula):
        self.nome=nome
        self.nota1=nota1
        self.nota2=nota2
        self.matricula=matricula
    def situacao(self,nota1,nota2):
        self.media=(nota1+nota2)/2
        print("a media é:",self.media)
        if self.media>=10:
            print("o aluno aprovou")
        else:
            print("o aluno reprovou")
aluno1=alunos("horacio",13608,12,17)
aluno1.situacao(10 ,19)