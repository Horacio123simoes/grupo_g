# Simulação de Multicaixa
# Horácio Simões
# 31 de outubro de 2023
from main import *
# -------barra de menu--------
title('SIMULAÇÃO DE MULTICAIXA')
print('\033[37m1 - Deposito Bancário\n2 - Consulta de Saldos\n3 - Levantamento na Conta\033[m')
#menuSelect = int(option('Sua opção[1, 2, 3]: '))
# -----Tratamento de menu-----

title('DEPOSITO BANCÁRIO')
numDaConta = option('Número da conta: ')
codPIN = int(option('Codigo PIN: '))
valorMonet = float(option('Valor Monetário: '))
access('Depósito Efectuado com Sucesso...')

title('CONSULTA DE SALDOS')
numDaContaOp = option('Número da conta: ')
codPINOp = int(option('Codigo PIN da conta: '))
if numDaContaOp == numDaConta and codPINOp == codPIN:
    print(f'\033[37mSAldo disponível: {valorMonet:.2f}\033[m')

    title('LEVANTAMENTO DE SALDO')
    numDaContaOp = option('Número da conta: ')
    codPINOp = float(option('Código PIN da conta: '))
    if numDaContaOp == numDaConta and codPINOp == codPIN:
        valorAlevantar = float(option('Valor a Levantar:'))
        resto = abs(valorAlevantar - valorMonet)

        title('RESULTADO')
        print(f'Número da conta: {numDaConta}\nValor levantado: {valorAlevantar:.2f}\nSaldo Inicial: {valorMonet:.2f}\nSaldo Atual: {resto:.2f}')
    else:
        print('Acesso negado, Número da Conta ou o PIN Errado')
else:
    print('Acesso negado, Número da Conta ou o PIN Errado')
