# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.# 
#Function
def datasheet(name = '<unknown>' ,goal = 0):
	print(f'Player {name} scored {goal} goal(s).')
	



#Main
n = str(input('Name: '))
g = str(input('Goals: '))
if g.isnumeric():
	g = int(g)
else:
	g = 0

if n.strip() == '':
	datasheet(goal = g)
else:
	datasheet(n, g)