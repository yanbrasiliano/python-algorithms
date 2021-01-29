#APOSTILA PYTHON PROGRESSIVO
# MAIOR - MENOR - SOMA DE VALORES

count = 0
list = []
while True:
	n = list.append(int(input('Enter a number: ')))
	count+=1
	
	'''	if count == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n '''

	option = ' '
	while option not in 'YN':
		option = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
	if option == 'N':
		break

print(f'{max(list)}')
print(f'{min(list)}')
print(f'{sum(list)}')