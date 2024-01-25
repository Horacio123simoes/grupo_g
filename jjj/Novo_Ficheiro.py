from Classe_Carro import Carro  # vai trazer a classe Carro criada noutro arquivo
from Classe_Proprietario import Proprietario  # vai trazer a classe Proprietário criada noutro arquivo

# Car=Carro("Toyota","LD-21-12-EM")criei o objeto Car
"""Prop=Proprietario("Euclides Moreira",930667788) #criei o objeto
#print(Carro)
#print("Marca:",Car.marca,"\nMatrícula:",Car.matricula)

#Associação de Classes:
"""

Car = Carro("Toyota", "LD-21-12-EM", 'Prop')  # este "Prop" refere-se ao objeto Proprietário

# Armazenar:

# Carros=[]
# Carros[0].marca
# Carros[0].matricula
# Carros[0].dono.nome
# Carros[0].dono.tel
# Implementar um cíclo para percorrer o vetor e implementar os elementos(carro ou proprietário)

# if Carros[0].dono.nome=="nome" pesquisar alguém

# teste do prof:
Carros = []


Prop = Proprietario("Antunes Viti", 928)
Car = Carro("Kia", "LD-47-12-AV", Prop)
Carros.append(Car)

Prop = Proprietario("Horácio Simons", 991)
Car = Carro("Kia", "LD-47-98-HS", Prop)
Carros.append(Car)
Carros.append(Car)

for ele in Carros:
    print(ele.marca)
    print(ele.matricula)
    print(ele.dono.nome)
    print(ele.dono.tel)
    print("==================================================================")
