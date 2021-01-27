#APOSTILA PYTHON PROGRESSIVO

# MAIOR E MENOR VALOR ENTRE X NÚMEROS.

c = b = l = 0

while True:
	n = int(input('Enter a number: '))
	c+=1
	if c == 1:
		b == l == n
	else:
		if n > b:
			b = n
		if n < l:
			l = n
	
	option = ' '
	while True:
			option = str(input('CONTINUE?[Y/N]: ')).upper().split()[0]
			if option in 'YN':
					break
			print('ERROR! Try Again.')
	if option == 'N':
			break
print('*'*20)
print(f'Max value: {b} and Min value: {l}.')

print('*'*20)