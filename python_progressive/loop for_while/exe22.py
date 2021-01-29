##Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

n = int(input('Enter a number: '))

m = 0

for count in range(2,n):
	if n % count == 0:
		print(f'{count}', end='')
		m+=1
if m == 0:
	print('It is prime.')
else:
	print(f'\nHave {m} multiple above 2 and below of the {n}.')