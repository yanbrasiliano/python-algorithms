#APOSTILA PYTHON PROGRESSIVO

# MAIOR E MENOR VALOR ENTRE X NÚMEROS.



while True:
	n = int(input('Enter a number: '))
	b = l = 0

	if b == n:
		n = b
	elif b > n:
		n = b
	if l == n:
		n = l
	elif l < n:
		n == l

	option = ' '
	while True:
			option = str(input('CONTINUE?[Y/N]: ')).upper().split()[0]
			if option in 'YN':
					break
			print('ERROR! Try Again.')
	if option == 'N':
			break
	
print('*'*20)
print(f'Highest value: {b}.')
print(f'Lowest value: {l}.')
print('*'*20)