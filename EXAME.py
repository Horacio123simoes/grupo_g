# programa: calculo de pagamento de credito bancario
# data: 10/03/2023
# autor: Domingos
from datetime import date

# criação variavel

conta_bancaria = int(input("digita o numero da conta: "))
nome_cliente = input("digita o nome cliente: ")
valor_credito_casa = float(input("digita o valor em que está avaliado a tua casa: "))
salario = float(input("digita o teu salario: "))
anos_pagamento = int(input("digita os anos de pagamento: "))
data_credito = input("digita a data do credito(DD/MM/AAAA: ").split("/")
data_credito2 = date(int(data_credito[2]),int(data_credito[1]),int(data_credito[0]))

# calculo valor credito
valor_credito_por_mes = valor_credito_casa / (anos_pagamento * 12)
percentagem = (salario * 30 / 100)
if valor_credito_por_mes > percentagem:
    print("credito recusado")
else:
    print("credito aceite")
    data_pagamento_credito = input("digita a data de pagamento do credito(DD/MM/AAAA: ").split("/")
    data_pagamento_credito2 = date(int(data_pagamento_credito[2]),int(data_pagamento_credito[1]),int(data_pagamento_credito[0]))
    prazo = (data_pagamento_credito2 - data_credito2).days
    if (prazo > 10 and prazo < 30):
        juro = valor_credito_por_mes * 5 / 100
    elif prazo > 30:
        juro = valor_credito_por_mes * 10 / 100
    else:
        juro = 0
    valor_credito_por_mes = valor_credito_por_mes+ juro
print("valor apagar por mes: {}".format(valor_credito_por_mes))
print("Os 30% do salario: {}".format(percentagem))