#frutas=["manga","banana","maça"]
#frutas.append("ananas")
#frutas.insert(1,"uva")
#frutas.sort()
#print(frutas)
#print(f"essa lista tem {len(frutas)} elementos")


#usuario="horacio"
#senha=1234
#print("seja benvindo")
#print("usuario: ")
#usuario= input()
#print("senha: ")
#senha= input()
#if (usuario== "horacio") and (senha==1234):
    #print("benvindo ao pograma")
#else:
   # print("senha do usuario invalida! ")

usuario="admin"
senha=123
usuario=input("insere o nome: ")
if(usuario=="admin"):
    senha = input("insere a senha: ")
    if (senha==123):
        print("benvindo ao sistema")
else:
    print("login invalido!")
