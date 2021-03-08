"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

"""

#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta

dates = []

#função para médias.
def average(a,b):
	
	return (a+b)/2

while True:
	#capturando os dados
	name = str(input('Name: '))
	note_1 = float(input('First note: '))
	note_2 = float(input('Second note: '))
	
	#Boletim contendo a média de cada um.
	t = average(note_1,note_2)
	
	#adicionando os dados a lista.
	dates.append([name,[note_1,note_2],t])

	#While para adicionar mais dados a lista, caso queira sair, digite N ou n.
	resp = ' '
	while resp not in 'YN':
		resp = str(input('Register one more? [Y/N]')).upper().strip()
	if resp == 'N':
		break
print(dates)
print()
for i,s in enumerate(dates):
	print(f'{i:<5}{s[0]:<10}{s[2]:<10}')
print()

while True:
	op = int(input('Show student grade N - 999 = break >>  '))
	if op == 999:
		break
	if op <= len(dates) -1:
		print(f'Note {dates[op][0]} is {dates[op][1]}')

	