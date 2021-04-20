#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

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