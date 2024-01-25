class livro():
    def __init__(self,titulo,autor,pag):
        self.titulo=titulo
        self.autor=autor
        self.pag=pag
    def emprestar(self,vet):
        self.vet=["livro A","livro B","livro C"]
        self.vet.remove("livro A")
        print(self.vet)
        print("livro emprestado com sucesso")
    def devolucão(self):
        self.vet=["livro B","livro C"]
        self.vet.append("livro A")
        print(self.vet)
        print("livro devolvido com sucesso")
livro1=livro("the life","Simões",40)
livro1.emprestar("livro A")
livro1.devolucão()