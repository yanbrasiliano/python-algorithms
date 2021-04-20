# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from math import e
from random import randint
print('~'*25)
print('Let\'s play PAR or ÍMPAR! ')
print('~'*25)

v = 0

while True:
    jogador = int(input('Enter the value: '))
    computador = randint(0, 21)
    total = jogador + computador
    escolha = ' '
    escolha = str(input('Par ou Ímpar?[P/I]: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar?[P/I]: ')).strip().upper()[0]
    print(f'You played {jogador} and The Computer played {computador}.\nTotal: {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Congratulations, you win!')
            v += 1
        else:
            print('You loss, try again.')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Congratulations, you win!')
            v += 1
        else:
            print('You loss, try again.')
            break
print(f'GAME OVER! You won {v} times.')
