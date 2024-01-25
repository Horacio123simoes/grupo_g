from random import randint
from time import sleep
computador=randint(0,5)
print("eu o computador estou a divinhar...")
print("*"*20)
print("computador pensando...")
sleep(4)
jogador=int(input("o numero do jogador e?:"))
print("computador adivinhou:{},o jogador adivinhou:{},".format(computador,jogador))
if(computador==jogador):
    print("jogador acertou")
else:
    print("o jogador nao acrertou"
          "")
