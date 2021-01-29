##Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

'''n = int(input('Enter a number: '))

m = 0

for count in range(2,n-1):
	if n % count == 0:
		print(f'{count}', end='')
		m+=1
if m == 0:
	print('It is prime.')
else:
	print(f'\nHave {m} multiple above 2 and below of the {n}.')'''


n = int(input('Enter a number: '))

while True:
	if n % 2 == 0 and n != 2:
		print('NO PRIME')
		break
	else:
		print('PRIME.')
		break
for c in range(n):
	if n % (c + 1) == 0:
		 