import os

print("""
               Menu

             (1) Balcão
             (2) ATM
             (3) Sair
      """)

menu = int(input("Escolha: "))
os.system("cls") # Limpa Tela


if menu == 1:
    print("""Seja Bem-Vindo/a ao Balcão
          
              (1) Abrir uma Conta
              (2) Consultar Conta Clientes
              (3) Fechar Conta
              (4) Bloquear Conta
              (5) Deposito
              (6) Levantamento
              (7) Sair
          """)
    menu2 = int(input("Escolha: "))
    os.system("cls")
    if menu2 == 1:
        print("*Abrir uma Conta*")
        
        nome_cliente = str(input("Nome Completo: "))
        idade = int(input("Idade: "))
        if idade < 18:
            print("Menor de idade!")
        else:
         n_bilhete = int(input("N Bilhete: "))
         morada = str(input("Morada: "))
         nome_mae = str(input("Nome da mae: "))
         nome_pai = str(input("Nome do Pai: "))
         
         os.system("cls")
         
         print(f"""
                Conta Aberta com sucesso!
                Seja Bem-Vindo/a {nome_cliente}
                
                *Seus Dados*
                Nome: {nome_cliente}

            
               """)
    elif menu2 == 2:
        print("""
                *Consulta Conta Clientes*
              """)   
    elif menu2 == 3:
        print("*Fechar Conta*")
     
    elif menu2 == 4:
        print("*Bloquear Conta*")
        
    elif menu2 == 5:
        print("*Deposito*")
        
    elif menu2 == 6:
        print("Levantamento")
    elif menu == 7:
        os.system("cls")
    # FIM DO MENU 2
    
elif menu == 2:
    print("""ATM
          
             (1) Transferências
             (2) Consultas
             (3) Levantamento
             (4) Sair
        """)
    menu3 = int(input("Escolha: "))
    if menu3 == 1:
        print("""*Transferências*
                  
              """)
    elif menu3 == 2:
        print("*Consultas*")
    elif menu3 == 3:
        print("*Levantamento*")
    elif menu3 == 4:
        os.system("cls")
    # FIM DO MENU 3
    
elif menu == 3:
    os.system("cls")
else:
    print("Inválido")