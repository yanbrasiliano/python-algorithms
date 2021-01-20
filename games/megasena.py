#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint
tot = 1

list = []
games = []
print('-'*30)
print('\tGAME MEGA SENA')
print('-'*30)
g = int(input('How many games do you want? [->]: '))

while tot <= g:
	cont = 0
	while True: 
		num = randint(0,60)
		if num not in list:
			list.append(num)
			cont+=1
		if cont >= 6:
			break

	list.sort()
	games.append(list[:])
	list.clear()
	tot+=1
print(f'-=-		DRAWING {g} GAMES		')
for i,l in enumerate(games):
	sleep(2)
	print(f'Game - {i+1}: {l}')


