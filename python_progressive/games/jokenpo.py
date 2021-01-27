# jogo pedra,papel ou tesoura.
from random import randint
from time import sleep
# lógica do computador para jogar o jogo, de forma sorteada.
#		        0      1          2
items = ('Stone', 'Paper', 'Scissors')
computer = randint(0, 2)

print('\tJOKENPO')
# escolha do usuário para o jogo.
print('\n')

print(''' Options:
[1]- Stone.
[2]- Paper.
[3]- Scissors. ''')
print('\n')

name = str(input(('Player name: ')))
player = int(input('Your choice is: '))
print('\n')


print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)


# escolhas definidas.
print('*' * 15)
print('Computer choice {}.'.format(items[computer]))
print('Player choice: {}.'.format(items[player]))
print('*' * 15)


# lógica para resultados.
if computer == 0:  # computer choose stone.
    if player == 0:
        print('GAME DRAW!')
    elif player == 1:
        print('{} WIN!' .format(name))
    elif player == 2:
        print('COMPUTER WIN!')
    else:
        print('Invalid choice. Try again!')


elif computer == 1:  # computer choose paper.
    if player == 0:
        print('COMPUTER WIN!')
    elif player == 1:
        print('GAME DRAW!')
    elif player == 2:
        print('{} WIN!')
    else:
        print('Invalid choice. Try again!')

elif computer == 2:  # computer choose scissors.
    if player == 0:
        print('{} WIN!'.format(name))
    elif player == 1:
        print('COMPUTER WIN!')
    elif player == 2:
        print('GAME DRAW!')
    else:
        print('Invalid choice. Try again!')
