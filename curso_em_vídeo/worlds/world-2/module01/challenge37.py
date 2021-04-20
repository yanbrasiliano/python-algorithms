# programa receberá um valor e pergunará se o usuário quer converter para binário, octal ou hexadecimal.
from time import sleep
while True:
	print('*' * 15)
	print('\tNUMBER BASE CONVERTER')
	print('*' * 15)

	n = int(input('Enter the number: '))

	print('''Choose the option:\n
	[1]- Binary
	[2]- Octal
	[3]- Hexadecimal''')

	option = int(input('\nNumber: '))

	print('\n')
	print('\tConverting...')
	sleep(2)

	if option == 1:
			print('{} converted to binary is {}.'.format(n, bin(n)[2:]))
	elif option == 2:
			print('{} converted to octal is: {}.'.format(n, oct(n)[2:]))
	elif option == 3:
		print('{} converted to hexadecimal is {}.'.format(n,hex(n)[2:]))
	else:
		print('Option invalidates, return to the menu.')
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
			break