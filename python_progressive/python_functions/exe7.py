#Fatorial com função recursiva
#Somatório com funções recursivas.

def factori(x):
	if x == 1:
		return 1
	else:
		return x * factori(x - 1)

while True:
	y = int(input('Factorial of: '))
	z = factori(y)
	print(f'Total: {z}.')