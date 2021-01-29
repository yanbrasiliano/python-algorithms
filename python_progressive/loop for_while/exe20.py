#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores 
from time import sleep
import math
#variáveis iniciadas.
c = 1
r = 1

# repete até digitar valor invalido.
while True:
	#entrada de valores.
	f = int(input('Factorial of: '))
	
	#condição para fatoração.
	'''	while c <= f:
			r *=c
			c +=1'''
	while f > 0 and f < 16:
		print(f'Calculating factorial of {f}...')
		sleep(1)
		print(f'{f}! = {math.factorial(f)}.')
		break
	else: 
		print('ERROR')
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break