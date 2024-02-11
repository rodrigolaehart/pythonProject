from random import randint

computador = randint(0, 5)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABENS: Você conseguiu me vencer! ')
else:
    print(f'GANHEI, eu pensei no número {computador} e não no {jogador}!')