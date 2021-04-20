from random import randint
from time import sleep
from operator import itemgetter

#dicionário para receber números aleatórios dos jogadores.
game = {
'player1': randint(1,6),
'player2': randint (1,6),
'player3': randint (1,6),
'player4': randint (1,6) }

#lista para receber o ranking dos jogadores
rank = list()

print('SORTED VALUES: ')
for k,v in game.items():
	print(f'{k} - {v}')
	sleep(1)
rank = sorted(game.items(), key = itemgetter(1), reverse=True)

for i,v in enumerate(rank):
	print(f'{i+1}° Position: {v[0]} with {v[1]} points.')
	sleep(1)