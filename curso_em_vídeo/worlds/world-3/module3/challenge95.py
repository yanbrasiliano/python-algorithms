#Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.



tot = 0
player = dict()
games = list()
player['name'] = str(input('Enter name: '))
x = int(input(f'Enter the games played of the {player["name"]}: '))
for c in range(0,x):
	games.append(int(input(f'Goals in {c+1}° match: ')))

''' FORMATO 1'''
print('-=-'*20)
player['goals'] = games[:]
player['tot'] = sum(games)
print(f'{player}')
print('-=-'*20)
''' FORMATO 2'''
for k,v in player.items():
	print(f'In the position {k} has value {v}.')

print('-=-'*20)
''' FORMATO 3'''
print(f'the player {player["name"]} played {x} games.')

for pos,c in enumerate(games):
	print(f'{player["name"]} - {pos + 1}° game: {c} goals')
print('-=-'*20)