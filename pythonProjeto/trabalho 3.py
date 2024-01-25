"""class banco():
    def __init__(self,nome,numero):
        self.nome=nome
        self.numero=numero"""

"""class Cliente:
    def _init_(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

    def _str_(self):
        return f"{self.nome} {self.sobrenome} - {self.email}"

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    email = input("Digite o email do cliente: ")

    novo_cliente = Cliente(nome, sobrenome, email)
    lista_clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!\n")

# Lista para armazenar os clientes
lista_clientes = []

# Menu principal
while True:
    print("1. Cadastrar novo cliente")
    print("2. Mostrar lista de clientes")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        print("\nLista de Clientes:")
        for cliente in lista_clientes:
            print(cliente)
        print()
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

    # Criando alguns objetos Cliente
    cliente1 = Cliente("João", "Silva", "joao@email.com")
    cliente2 = Cliente("Maria", "Souza", "maria@email.com")
    cliente3 = Cliente("Carlos", "Ferreira", "carlos@email.com")

    # Criando uma lista de clientes
    lista_clientes = [cliente1, cliente2, cliente3]

    # Mostrando a lista de clientes
    print("Lista de Clientes:")
    for cliente in lista_clientes:
        print(Cliente)"""