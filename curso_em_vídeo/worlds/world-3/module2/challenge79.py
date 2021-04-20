#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

value = list()
while True:
		x = int(input(f'Enter a value: '))
		if x not in value:
			value.append(x)
			print('VALUE SUCCESSFULLY REGISTERED.')
		else:
			print("Duplicate value, try again.")	

		opção = ' '
		while opção not in 'YN':
			opção = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
		if opção == 'N':
				break
print(f'Order is {sorted(value)}')