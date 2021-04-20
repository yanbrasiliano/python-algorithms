#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep

record = list()
while True:
	name = str(input('Name: '))
	n1 = float(input('Note 1: '))
	n2 = float(input('Note 2: '))
	media = (n1+n2)/2
	record.append([name,[n1, n2], media])
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break
print('*'*30)

print(f'{"N.":<10}{"NAME":<10}{"NOTE":<6}')

print('*'*30)
for l, c in enumerate(record):
	print(f'{l:<10}{c[0]:<10}{c[2]:<6.1f}')

while True:
	print('*'*35)
	x = int(input('Show student grades[N.] [999-STOP]: '))
	if x == 999:
		sleep(1)
		print('Finishing...')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		break
	if x <= len(record) - 1:
		print(f'Notes of {record[x][0]} are {record[x][1]}.')
