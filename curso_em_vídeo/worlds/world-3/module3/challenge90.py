# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

student = dict()

while True:
	student['name'] = str(input('Student: '))
	student['media'] = float(input('Media: '))
	print()
	if 	student['media'] >= 11 or student['media'] < 0:
		print('Unrecognized value, TRY AGAIN.')
		student['media'] = float(input('Media: '))
	print('=~='*30)
	if student['media'] < 7:
		print(f'- Media of the {student["name"]} is {student["media"]}.')
		print('- Situation: Reproved, Try again!')
	else:
		print(f'- Media of the {student["name"]} is {student["media"]}.')
		print('- Situation: Congratulations,Approved!')
		print()
	option = ' '
	while option not in 'YN':
		option = str(input('CONTINUE? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break
print('thanks,bye!')