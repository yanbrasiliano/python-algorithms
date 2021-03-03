"""
Crie um jogo em Python onde o computador vai sortear um número de 1 até
100.
Em seguida, você vai tentar adivinhar que número foi esse.
A cada tentativa, ele vai te dizer se seu palpite foi alto, baixo ou se você
acertou.
Quando acertar, deve mostrar quantas tentativas você fez até acertar.
"""

from random import randint
from time import sleep


def generator():
    return randint(1, 10)


def game():
    computer_logic = generator()
    print()
    print('Jarvis is choosing a number between 0 and 10... ')
    sleep(1.5)
    print('Jarvis choose a number, now it\'s your turn. ')
    attempts = 0  # armazena as tentativas do usuário.
    t = 0
    while t is not computer_logic:
        print()
        t = int(input('Enter your choice: '))  # escolha do jogador.
        attempts += 1
        if t > computer_logic:
            print('You have entered a number greater than the one drawn. ')
        elif t < computer_logic:
            print('You entered a number less than the one drawn.')
        else:
            print(
                f'Congratulations!\nYou typed {t} and computer choose {computer_logic}.\nAttempts: {attempts}.')


while True:
    game()
