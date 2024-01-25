
clientes=[]
contas=[]

def cadastrar():
    
    while True:
        print("========     ========")
        print("      HS BANK      ")
        print("     = = = = = =     ")
        print("  CADASTRAR CLIENTE  ")
        print(" ====================")
        print("")
        print("Informe os dados do cliente")

        dadoscadastro={}

        dadoscadastro["nomecompleto"] = (input("nome:"))
        dadoscadastro["sexo"] = (input("sexo:"))
        dadoscadastro["datadenascimento"] = (input("datadenascimento:"))

        dadoscadastro["numeroBI"] = input("numeroBI:")
        lista = {i["numeroBI"]: i for i in clientes}
        
        while dadoscadastro["numeroBI"] in lista:
            dadoscadastro["numeroBI"] = input("Bilhete em uso tente novamente")
        clientes.append(dadoscadastro)
        print ("OK Cadastro concluido")
        opcao= input("Deseja cadastrar mais cliente? (S/N) ").strip().lower()
        import os
        os.system("cls")
        if (opcao=="n"):
            menu()
            break
def Abertura():

    while True:


        print("Indroduz o numero do bilhete do cliente")
        lista = { i ["numeroBI"]: i for i in clientes}
        buscar = input("numeroBI")
        print("====================")
        print(" ABERTURA DE CONTA  ")
        print("A)--> Conta Poupança")
        print("B)--> Conta Corrente")

        if buscar in lista:

            print("Indroduz os dados para a abertura da conta")

            dadosconta={}
            dadosconta["id"]=buscar
            dadosconta["numerodaconta"]=input("numerodaconta:")
            dadosconta["IBAN"]=input("IBAN:")
            dadosconta["cidade"]=input("cidade:")
            dadosconta["telefone"]=input("telefone:")
            contas.append(dadosconta)
        else: 
            print("Cliente não cadastrado, cadastre primeiro")
        
        opcao= input("Deseja fazer abertura de outro cliente? (S/N) ").strip().lower()
        if (opcao=="n"):
            menu()
            break


def bloquear():
    print("====================")
    print("   BLOQUEAR CONTA   ")
def eliminar():
    print("====================")
    print("   ELIMINAR CONTA   ")
def sair():
    print("FIM")
    
def menu():
    print("========     ========")
    print("      HS BANK      ")
    print("     = = = = = =     ")
    print("[1] Cadastrar Cliente")
    print("[2] Abertura de conta")
    print("[3] Bloquear Conta")
    print("[4] Eliminar Conta")
    print("[0] Sair")

menu()
while True:
    x = int(input("Escolha OPÇÃO :"))
    while x > 4 or x < 0:
            x = int(input("[Erro tente novamente] Escolha uma opção valida"))
    import os 
    os.system("cls")

    if x==1:
        cadastrar()
    elif x==2:
        Abertura()
    elif x==3:
        bloquear()
    elif x==4:
        eliminar()
    elif x==0:
        sair()
    else:
        print ("Programa encerrada")
    break






