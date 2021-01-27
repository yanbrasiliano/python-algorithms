#Fatorial
from time import sleep
#variáveis iniciadas.
c = 1
r = 1

# repete até digitar valor invalido.
while True:
	#entrada de valores.
	f = int(input('Factorial of: '))
	print(f'Calculating factorial of {f}...')
	sleep(1)
	#condição para fatoração.
		while c <= f:
		r *= c
		c +=1
	print(f'{f}! = {r}.')
	
	x = ' '
	while x not in 'YN':
		x = str(input('CONTINUE? [Y/N]')).strip().upper()
		if x == 'N':
			break
	print('Thanks!')