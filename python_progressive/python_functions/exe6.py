#Somatório com funções recursivas.

def som(x):
	if x == 1:
		return 1
	else:
		return x + som(x-1)

while True:
	y = int(input('Sum of 1 to: '))
	z = som(y)
	print(f'Total: {z}.')