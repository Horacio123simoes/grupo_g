class armazenar():
    def __init__(self,nome,sexo,telefone,endereco):
        self.nome=nome
        self.sexo=sexo
        self.telefone=telefone
        self.endereco=endereco

    def guardar(self):
        self.dados = []
        self.dados=self.vet
        self.vet=self.nome=input("insere o nome")
        self.vet = self.sexo = input("insere o sexo")
        self.vet = self.telefone = int(input("insere o telefone"))
        self.vet = self.endereco = input("insere o endereco")
        self.dados.append(self.vet)

    def ver(self):
        self.dados=self.vet
        print(self.dados)

resultado=armazenar("j","m",96777,"cacuaco")
resultado.guardar()
resultado.ver()