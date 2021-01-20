#11. Altere o programa anterior para mostrar no final a soma dos números.

soma = 0 
n1 = int(input('Enter a 1° value: ')) 
n2 = int(input('Enter a 2° value: ')) 

while n2 < n1:
	print('Try again, first number cannot be greater than second number.')
	n1 = int(input('Enter a 1° value: ')) 
	n2 = int(input('Enter a 2° value: ')) 
	if n1 < 0 or n2 < 0:
		break

else:
	print('*'*30)
	for c in range(n1 + 1,n2,1):
		soma+=c
		print(f'Interval between {n1} and {n2}: [{c}]')


print(f'Interval sum total: {soma}')

print('*'*30)