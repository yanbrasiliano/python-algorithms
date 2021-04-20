try:
	a = int(input('Number: '))
	b = int(input('Denominator: '))
	x = a / b
except Exception as error:
	print(f'ERROR!\nDescription {error.__class__}')
else:
		print(f'Result: {x}')
finally:
	print('Bye Bye :)')