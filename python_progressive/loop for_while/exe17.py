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
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break