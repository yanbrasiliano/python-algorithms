#13. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


def cont(x):
	count = len(x)
	return count

def menu():
	num = str(input('Enter a number: '))
	print(f'The total number of digits is: {cont(num)}')

while True:
	menu()