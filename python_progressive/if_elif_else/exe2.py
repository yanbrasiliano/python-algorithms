#APOSTILA PYTHON PROGRESSIVO

# MAIOR E MENOR VALOR ENTRE X NÚMEROS.

b = l = 0

while True:
	n = int(input('Enter a number: '))

	option = ' '
	while True:
			option = str(input('CONTINUE?[Y/N]: ')).upper().split()[0]
			if option in 'YN':
					break
			print('ERROR! Try Again.')
	if option == 'N':
			break