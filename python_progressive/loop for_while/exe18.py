#APOSTILA PYTHON PROGRESSIVO
# MAIOR - MENOR - SOMA DE VALORES

maior = menor = soma = 0
while True:
	n = int(input('Enter a number: '))
	soma+=n
	x = max(n)
	y = min(n)
	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break

print(f'{soma}')
print(f'{max(x)}')
print(f'{min(y)}')