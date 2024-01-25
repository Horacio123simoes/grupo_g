# Autor: Horácio Simões
# Data: 16/02/2023
# Nome do programa: Calculo do crédito

from datetime import date

conta_bancaria = input("digite conta bancaria: ")
nome_do_cliente = input("digite o nome do cliente: ")
valor_credito_casa = int(input("digite o valor do credito da casa: "))
salario = float(input("digite o salario: "))
anos_de_pagamento = int(input("digite os anos a pagar: "))
data_credito = input("digite data credito DD/MM/AAAA: ").split("/")
data_de_pagamento = input("digite data pagar DD/MM/AAAA: ").split("/")
data_credito2 = date(int(data_credito[2]),int(data_credito[1]),int(data_credito[0]))
data_de_pagamento2 = date(int(data_de_pagamento[2]),int(data_de_pagamento[1]),int(data_de_pagamento[0]))
salario_minimo = (salario*30)/100
credito_mes = valor_credito_casa/(anos_de_pagamento*12)

if credito_mes>salario_minimo:
    print("credito recusado")
else:
    print("credito concedido")
prazo=(data_de_pagamento2-data_credito2).days
if prazo>10 and prazo<30:
    juro=(credito_mes*5)/100
    print(f"juro {juro:2f}")
else:
    juro=(credito_mes*10)/100
    print(f"juro{juro:2f}")
valor_pagamento_mes=credito_mes+juro+salario_minimo

#mostrar:
print(f"|conta bancaria:{conta_bancaria}  |")
print(f"|nome do cliente:{nome_do_cliente} |")
print(f"|valor dc casa:{valor_credito_casa} |")
print(f"|salario:{salario} |")
print(f"|anos:{anos_de_pagamento} |")
print(f"|data de credito:{data_credito} |")
print(f"|data de pagamento:{data_de_pagamento} |")
print(f"|prazo:{prazo} |")
print(f"|o numero d mes:{credito_mes} |")
print(f"|valor pagar:{valor_pagamento_mes} |")
print(f"|salario:{salario} |")
print(f"|anos:{anos_de_pagamento} |")
print(f"|data de credito:{data_credito} |")
print(f"|data de pagamento:{data_de_pagamento} |")
print(f"|prazo:{prazo} |")
print(f"|o numero d mes:{credito_mes} |")
print(f"|valor pagar:{valor_pagamento_mes} |")
