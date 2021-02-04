# Calculadora com funções
def sum():
	a = float(input('First number: '))
	b = float(input('Second number: '))
	t = a + b
	print(f'{a} + {b} = {t}')


def subtraction():
	a = float(input('First number: '))
	b = float(input('Second number: '))
	t = a - b
	print(f'{a} - {b} = {t}')


def division():
	a = float(input('First number: '))
	b = float(input('Second number: '))
	t = a / b
	print(f'{a} / {b} = {t}')

def multiplication():
	a = float(input('First number: '))
	b = float(input('Second number: '))
	t = a * b
	print(f'{a} x {b} = {t}')


def potentiation():
	a = float(input('First number: '))
	b = float(input('Second number: '))
	t = a ** b
	print(f'{a} ^ {b} = {t}')


while True: 
	print('''
0 - Exit.
1. Sum.
2. Subtraction.
3. Division.
4. Multiplication.
5. Potentiation. ''')
	print()
	option = int(input('Option: '))

	if option == 0:
		print('thanks!')
		break
	if option == 1:
		sum()
	if option == 2:
		subtraction()
	if option == 3:
		division()
	if option == 4:
		multiplication()
	if option == 5:
		potentiation()
	if option > 5:
		print('ERROR 303\nTRY AGAIN!')
print()
print()