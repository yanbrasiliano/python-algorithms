#APOSTILA PYTHON PROGRESSIVO

# MAIOR E MENOR VALOR ENTRE X NÚMEROS.

from time import sleep

count = b = l = 0

while True:
	num = int(input('Enter a number: '))
	count+=1
	if count == 1:
		b=l=num
	else:
		if num > b:
				b=num	
		if num < l:
			l = num
	
	option = ' '
	while True:
			option = str(input('CONTINUE?[Y/N]: ')).upper().split()[0]
			if option in 'YN':
					break
			print('ERROR! Try Again.')
	if option == 'N':
			break

print('.')
sleep(1)
print('..')
sleep(1)
print('...')
sleep(1)
print('....')
sleep(1)
print('.....')
sleep(1)
print('......')
sleep(1)

print('*'*40)
print(f'Max value: {b} and Min value: {l}.')
print('*'*40)