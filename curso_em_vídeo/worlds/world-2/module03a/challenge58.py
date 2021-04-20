# usuário digitará um número e a maquina verificará se este número é o mesmo do que ela "pensou",o usuário tentará até acertar.

# VERSÃO COM WHILE!

from time import sleep
from random import randint

print('-_-' * 12)
print('\tGUESS MACHINE 2.0')
print('-_-' * 12)

# faz o sorteio dos números de 0 a 10
print('I am your machine and I thought of a number between 0 and 10.')
machine = randint(0, 10)  # faz o sorteio dos números de 0 a 10
print('\n')
acerto = False
guess = 0
# jogador faz a aposta do número até acertar.

print('PROCESSING....')

sleep(1)  # aguarda o tempo de 1 segundo para mostrar o resultado.
print('\n')

while not acerto:

	player = int(input('Enter your guess: '))
	guess +=1
	print('PROCESSING.....')
	sleep(0.5)
	print('\n')
	if player == machine:
		acerto = True
		
	else:
		if player < machine:
			print('Lower value, try again.')
		elif player > machine:
			print('Higher value try again.')

print('You Win with {} guesses; Congratulations!'.format(guess))

