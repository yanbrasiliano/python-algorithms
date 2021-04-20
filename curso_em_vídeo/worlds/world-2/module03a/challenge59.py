# programa pedirá para digitar dois números e lerá 4 opções para que ele seja executado conforme a opção desejada.

from time import sleep

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
option = 0

while option != 5:
			print('''[ 1 ] - Soma.
[ 2 ] - Multiplicação.
[ 3 ] - Maior entre os dois.
[ 4 ] - Novos números.
[ 5 ] - Exit.''')
			option = int(input('Your Option: '))

			if option == 1:
				s = n1 + n2
				print('Sum {} + {} = {}.'.format(n1, n2, s))
			elif option == 2:
				m = n1 * n2
				print('Multiplication {} * {} = {}.' .format(n1, n2, m))
			elif option == 3:	
				print('The biggest number between {} and {} is {}.'.format(n1,n2,max(n1, n2)))
			elif option == 4:
				print('New numbers!')
				n1 = int(input('Enter first number: '))
				n2 = int(input('Enter second number: '))
			elif option == 5:
				print('Finish...')
				sleep(2)
			else:
				print('Invalid Option, try again!')
				sleep(2)
print('Thanks, see you later!')
