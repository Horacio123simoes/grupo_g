

class Cliente:
    def _init_(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

    def _str_(self):
        return f"{self.nome} {self.sobrenome} - {self.email}"

# Criando alguns objetos Cliente
cliente1 = Cliente("João", "Silva", "joao@email.com")
cliente2 = Cliente("Maria", "Souza", "maria@email.com")
cliente3 = Cliente("Carlos", "Ferreira", "carlos@email.com")

# Criando uma lista de clientes
lista_clientes = [cliente1, cliente2, cliente3]

# Mostrando a lista de clientes
print("Lista de Clientes:")
for cliente in lista_clientes:
    print(cliente)