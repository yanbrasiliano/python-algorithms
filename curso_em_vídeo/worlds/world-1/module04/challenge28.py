# usuário digitará um número e a maquina verificará se este número é o mesmo do que ela "pensou".
from random import randint
from time import sleep
print('-_-' * 12)
print('\tGUESS MACHINE 1.0')
print('-_-' * 12)
# jogador faz a aposta do número.
player = int(input(
    'Hello, I am a machine that guesses things.\nThis version, i thinking a number and your will try to guess.\nWhat number am i thinking?[0-5]: '))

machine = randint(0, 5)  # faz o sorteio dos números de 0 a 5
print('\n')
# print('Your choose {} and I choose {}' .format(n, m))
print('PROCESSING....')
sleep(2) ## aguarda o tempo de 2 segundos para mostrar o resultado.
print('\n')

if player == machine:

    print('\tCONGRATULATIONS!\nYou guessed the number;\nI thought of the number {} and your type the number {}.' .format(machine, player))
    print('\n')

else:

    print('\tTRY AGAIN!\nI thought of the number {} and your type the number {}.' .format(
        machine, player))
    print('\n')
