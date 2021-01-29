#APOSTILA PYTHON PROGRESSIVO
# MAIOR - MENOR - SOMA DE VALORES

maior = menor = soma = count = 0
while True:
	n = int(input('Enter a number: '))
	soma+=n
	count+=1

	if count == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n

	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break

print(f'{soma}')
print(f'{maior}')
print(f'{menor}')