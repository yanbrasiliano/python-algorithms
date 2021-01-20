'''12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50'''
	
while True: 
	x = int(input('Enter number to multiply x10: '))
	for c in range(0,11):
		print(f'{x} x {c} = {x*c}' .format(x,c,x*c))
	option = ' '
	while option not in 'YN':
		option=str(input('Do you want to multiply another number?[Y/N]')).strip().upper()
	if option == 'N':
		break
print('thanks!')